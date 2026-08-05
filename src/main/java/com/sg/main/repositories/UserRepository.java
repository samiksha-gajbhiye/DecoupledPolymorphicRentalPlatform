package com.sg.main.repositories;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Integer> {

	// Finding user by attributes
	public Optional<User> findByEmail(String email);
	public Optional<User> findByName(String name);
	public Optional<User> findById(int id);

	// delete user by Usercode
	public Optional<User> findByUserCode(String userCode);
	public void deleteByUserCode(String userCode);
	public boolean existsByUserCode(String userCode);

	// delete user by id
	public boolean existsById(int id);

}