package com.sg.main.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Product;
import com.sg.main.entities.User;

import java.util.List;
import com.sg.main.entities.enums.AvailabilityStatus;



@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {

	
	//search product by different attribute 
	 List<Product> findByTitleIgnoreCase(String title);
	 List<Product> findByProductCode(String productCode);
	 List<Product> findByAvailability(AvailabilityStatus availability);
	 List<Product> findByTitle(String title);
	 List<Product> findByUser(User user);
	 List<Product> findByBrand(String brand);
	 List<Product> findByDescription(String description);
	 List<Product> findByLocation(String location);
	 
	 
	 
	
}
