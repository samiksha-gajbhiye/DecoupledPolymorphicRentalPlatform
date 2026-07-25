package com.sg.main.controller;


import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;
import com.sg.main.services.AuthService;
import com.sg.main.services.UserService;

import jakarta.transaction.Transactional;




@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/register")
public class UserController {

	@Autowired
	private UserService userService;
	
	@Autowired
	private AuthService authService;
	
	@PostMapping(value="/user" , consumes = org.springframework.http.MediaType.MULTIPART_FORM_DATA_VALUE )
	public User register(@RequestPart("user") User user, @RequestPart("profileImage") MultipartFile profileImage) throws IOException
	{
		return authService.registerUser(user, profileImage);
		
		
	}
	
	@Transactional
	@PutMapping("/update/{userCode}")
	public ResponseEntity<User> updateUser(@PathVariable String userCode , @RequestBody	 User user)
	{
		User updateUser = userService.UpdateUser(user, userCode);
		
		
		return  ResponseEntity.ok(updateUser);
	}
	
	@Transactional
	@DeleteMapping("/delete/{userCode}")
	public ResponseEntity<String> deleteUser(@PathVariable String userCode  )
	{
		String message =userService.deleteuser( userCode);
		return ResponseEntity.ok(message);
		
		
	}
	
}
