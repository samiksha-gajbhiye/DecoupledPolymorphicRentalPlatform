package com.sg.main.controller;

import java.io.IOException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Product;
import com.sg.main.entities.ProductImage;
import com.sg.main.services.ProductService;
import org.springframework.web.bind.annotation.GetMapping;


@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/product")
public class ProductController {

	@Autowired
	ProductService productService ;
	
	
	
	@PostMapping(value="/add", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
	public Product addProduct(
	        @RequestPart("product") Product product,
	        @RequestPart("images") List<MultipartFile> images) throws IOException {

	    return productService.registerProduct(product, images);
		
	}
	

	
	
	@GetMapping("/title/{title}")
	public ResponseEntity<List<Product>> getProductByTitle(@PathVariable String title)
	{
		
		
		List<Product> product = productService.GetProductDetailsByName(title);
		return ResponseEntity.ok(product);
		
	}
}
