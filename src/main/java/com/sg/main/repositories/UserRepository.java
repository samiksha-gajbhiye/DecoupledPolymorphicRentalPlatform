package com.sg.main.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.User;

@Repository
public interface UserRepository extends JpaRepository<User, Integer> {

}
