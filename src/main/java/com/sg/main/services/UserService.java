package com.sg.main.services;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Role;
import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;
import com.sg.main.repositories.roleRepository;

@Service
public class UserService {

	@Autowired
	private UserRepository userRepo;
	@Autowired
	private roleRepository roleRepo;
	
	public User registerUser(User user, MultipartFile profileImage) throws IOException
	{
		
		String uploadDir = "uploads/";

		File directory = new File(uploadDir);

		if (!directory.exists()) {
		    directory.mkdirs();
		}

		String fileName = System.currentTimeMillis() + "_"
		        + profileImage.getOriginalFilename();

		Path path = Paths.get(uploadDir, fileName);

		Files.write(path, profileImage.getBytes());

		user.setProfileImage(fileName);
		System.out.println(user);
	    System.out.println(user.getAddress());
	    System.out.println(user.getRole());
	    System.out.println(user.getRole().getId());
	    Role role = roleRepo.findById(user.getRole().getId())
	            .orElseThrow(() -> new RuntimeException("Role not found"));

	    user.setRole(role);
	    if(user.getAddress() != null) {

	        user.getAddress().forEach(address -> {
	            address.setUser(user);
	        });
	        
	        

	    }
		return userRepo.save(user);
	}
	
	
}
