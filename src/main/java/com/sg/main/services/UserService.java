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
	private UserRepository userRepository;
	
	public User UpdateUser(User updateUser , String userCode)
	{
		
						
	 User user = userRepository.findByUserCode(userCode)
			 			.orElseThrow(()-> new RuntimeException("User not found"));
	 
	 user.setName(updateUser.getName());
	 user.setEmail(updateUser.getEmail());
	 user.setPhone(updateUser.getPhone());
	 user.setProfileImage(updateUser.getProfileImage());
	 
	 return userRepository.save(user); 
	 
	}
	
	public String deleteuser( String userCode)
	{
			if(!userRepository.existsByUserCode(userCode))
			{
				throw new RuntimeException("User doesnt exist");
			}
			
			userRepository.deleteByUserCode(userCode);
		
			return "user deleted successfully";
			
				
	}

	
	
}
