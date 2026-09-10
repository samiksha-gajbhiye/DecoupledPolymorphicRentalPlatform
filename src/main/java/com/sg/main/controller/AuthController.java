package com.sg.main.controller;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.dto.LoginRequest;
import com.sg.main.dto.LoginResponse;
import com.sg.main.entities.User;
import com.sg.main.services.AuthService;

@RestController
@RequestMapping("/auth")
@CrossOrigin("*")
public class AuthController {

	@Autowired
	private AuthService service;

	//User Register

	@PostMapping(value="/register" , consumes = org.springframework.http.MediaType.MULTIPART_FORM_DATA_VALUE )
	public User register(@RequestPart("user") User user, @RequestPart("profileImage") MultipartFile profileImage) throws IOException
	{
		System.out.println();
		System.out.println("Controller reached");
		System.out.println("Password from Controller = " + user.getPassword());

		return service.registerUser(user, profileImage);


	}

	//User Login

	@PostMapping("/login")
public ResponseEntity<LoginResponse> login( @RequestBody LoginRequest request)
{
		System.out.println("Login hit success");
		LoginResponse response = service.LoginUser(request);
	return ResponseEntity.ok(response);
}

}
