package com.sg.main.services;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Address;
import com.sg.main.entities.Role;
import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;
import com.sg.main.repositories.roleRepository;

import org.springframework.security.crypto.password.PasswordEncoder;

@Service
public class AuthService {

	@Autowired
	private UserRepository userRepo;
	@Autowired
	private roleRepository roleRepo;
	
	@Autowired
	private PasswordEncoder passwordEncoder;
	
	public User registerUser(User user, MultipartFile profileImage) throws IOException
	{
		
		
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
	    if(user.getAddress() != null) {

	        user.getAddress().forEach(address -> {
	            address.setUser(user);
	        });
	        
	        
	        String userCode = "USR-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();

	        user.setUserCode(userCode);

	    }
	    user.setPassword(passwordEncoder.encode(user.getPassword()));
		return userRepo.save(user);  //sending hte user data to database
	}
	
	
	//Update the user information 
	
	
}
