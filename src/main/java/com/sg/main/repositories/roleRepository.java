package com.sg.main.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Role;


@Repository
public interface roleRepository extends JpaRepository<Role, Integer> {

	Optional<Role> findByRoleName(String roleName);
}
