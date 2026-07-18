package com.sg.main;


import java.lang.module.Configuration;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.sg.main.entities.User;


@SpringBootApplication
public class DemoRentalServicesApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoRentalServicesApplication.class, args);
	
		User user = new User();
		user.toString();
		
		
		
		
	}

}
