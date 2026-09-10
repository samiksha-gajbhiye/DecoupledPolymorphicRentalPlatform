package com.sg.main.services;

import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import com.sg.main.entities.User;
import com.sg.main.repositories.UserRepository;

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

	public Optional<User> findUser(String email)
	{
		if(!userRepository.existsByEmail(email))
		{
			throw new UsernameNotFoundException("USer does not exist");
		}
			Optional<User> user = userRepository.findByEmail(email);

			return user;
	}




}
