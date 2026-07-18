package com.sg.main.controller;


import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;
import com.sg.main.services.UserService;




@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/register")
public class UserController {

	@Autowired
	private UserService userService;
	
	@PostMapping(value="/user" , consumes = org.springframework.http.MediaType.MULTIPART_FORM_DATA_VALUE )
	public User register(@RequestPart("user") User user, @RequestPart("profileImage") MultipartFile profileImage) throws IOException
	{
		return userService.registerUser(user, profileImage);
		
		
	}
	
}
