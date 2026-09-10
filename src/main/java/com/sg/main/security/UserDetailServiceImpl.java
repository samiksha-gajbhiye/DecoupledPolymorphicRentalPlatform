package com.sg.main.security;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;

@Service
public class UserDetailServiceImpl implements UserDetailsService {

	@Autowired
	private UserRepository userRepository;

	@Override
	public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
		// TODO Auto-generated method stub


			User user =userRepository.findByEmail(email)
					.orElseThrow(()->new UsernameNotFoundException("Email doesnt exist"));


			return org.springframework.security.core.userdetails.User
			        .withUsername(user.getEmail())
			        .password(user.getPassword())
			        .roles(user.getRole() != null ? user.getRole().getRoleName().toUpperCase() : "USER")
			        .build();
	}



}
