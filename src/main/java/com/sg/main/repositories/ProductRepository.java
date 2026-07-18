package com.sg.main.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Product;

@Repository
public interface ProductRepository extends JpaRepository<Product, Integer> {

}
