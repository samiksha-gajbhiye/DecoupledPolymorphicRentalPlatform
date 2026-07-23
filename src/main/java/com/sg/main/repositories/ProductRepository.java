package com.sg.main.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Product;
import java.util.List;


@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {

	 List<Product> findByTitleIgnoreCase(String title);
	
}
