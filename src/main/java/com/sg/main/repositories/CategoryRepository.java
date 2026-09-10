package com.sg.main.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Category;
import com.sg.main.entities.Product;


@Repository
public interface CategoryRepository extends JpaRepository<Category, Integer> {

	List<Product> findByName(Category category);

}
