package com.sg.main.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.entities.Product;
import com.sg.main.entities.ProductImage;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/product")
public class ProductController {

	public Product registerProduct(@RequestPart Product product , @RequestPart ProductImage pImage)
	{
		
		
		return product;
		
	}
}
