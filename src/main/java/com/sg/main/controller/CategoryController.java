package com.sg.main.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.entities.Category;
import com.sg.main.repositories.CategoryRepository;

@RestController
@RequestMapping("/category")
public class CategoryController {

	@Autowired
	private CategoryRepository categoryRepository;

	
	@GetMapping("/all")
	public ResponseEntity<List<Category>> getAllCategories()
	{
		return ResponseEntity.ok(categoryRepository.findAll());
	}
}
