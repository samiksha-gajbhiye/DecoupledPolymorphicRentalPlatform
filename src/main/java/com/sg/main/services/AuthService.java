package com.sg.main.services;

import java.io.Console;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.dto.LoginRequest;
import com.sg.main.dto.LoginResponse;
import com.sg.main.entities.Address;
import com.sg.main.entities.Role;
import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;
import com.sg.main.repositories.roleRepository;
import com.sg.main.security.JwtUtil;


@Service
public class AuthService {

	@Autowired
	private UserRepository userRepo;
	@Autowired
	private roleRepository roleRepo;
	@Autowired
	private PasswordEncoder passwordEncoder;
	@Autowired
	private AuthenticationManager authenticationManager;
	@Autowired
	 private JwtUtil jwtUtil; 
	
	public User registerUser(User user, MultipartFile profileImage) throws IOException
	{
		
		
		if(userRepo.findByEmail(user.getEmail()).isPresent()) {
		    throw new RuntimeException("Email already exists");
		}

	    user.setPassword(passwordEncoder.encode(user.getPassword()));
		System.out.println(user.getPassword());
		
	//uploading the  user image to local folder 
		String uploadDir = "uploads/";

		File directory = new File(uploadDir);

		if (!directory.exists()) {
		    directory.mkdirs();
		}

		
	//setting file name for the image
		String fileName = System.currentTimeMillis() + "_"
		        + profileImage.getOriginalFilename();

		Path path = Paths.get(uploadDir, fileName);

		Files.write(path, profileImage.getBytes());

		user.setProfileImage(fileName);
	/*	System.out.println(user);
	    System.out.println(user.getAddress());
	    System.out.println(user.getRole());
	    System.out.println(user.getRole().getId());
	    
	*/
		
	//setting the role of the user (admin , owner , renter)
	    Role role = roleRepo.findById(user.getRole().getId())
	            .orElseThrow(() -> new RuntimeException("Role not found"));

	    user.setRole(role);
	    
	    String userCode = "USR-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();

        user.setUserCode(userCode);
	    
	    if(user.getAddress() != null) {

	        user.getAddress().forEach(address -> {
	            address.setUser(user);
	        });
	        
	        
	        

	    }
	    
	    
		return userRepo.save(user);  //sending hte user data to database
	}
	
	//user Login
	
	public LoginResponse LoginUser(LoginRequest request) {


	    Authentication authentication =
	            authenticationManager.authenticate(
	                    new UsernamePasswordAuthenticationToken(
	                            request.getEmail(),
	                            request.getPassword()
	                    )
	            );

	    String token = jwtUtil.generateToken(request.getEmail());

	    String role = authentication.getAuthorities()
	            .stream()
	            .findFirst()
	            .map(authority -> authority.getAuthority())
	            .orElse("ROLE_USER");

	    return new LoginResponse(
	            "Login successful",
	            token,
	            authentication.getName(),
	            role
	);
	    
	   
	}
	
}
