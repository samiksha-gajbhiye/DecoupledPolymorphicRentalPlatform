package com.sg.main.controller;

import java.io.IOException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Product;
import com.sg.main.services.ProductService;



@RestController
@RequestMapping("/product")
public class ProductController {

	@Autowired
	ProductService productService ;


	@PreAuthorize("hasAnyRole('OWNER','USER')")
	@PostMapping(value="/add", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
	public Product addProduct(
	        @RequestPart("product") Product product,
	        @RequestPart("images") List<MultipartFile> images, Authentication authentication) throws IOException {

	    return productService.registerProduct(product, images, authentication);

	}




	@GetMapping("/title/{title}")
	public ResponseEntity<List<Product>> getProductByTitle(@PathVariable String title)
	{
		System.out.println("Reach controller");

		List<Product> product = productService.GetProductDetailsByName(title);
		return ResponseEntity.ok(product);

	}

	@GetMapping("/category/{category}")
	public ResponseEntity<List<Product>> findByCategory(
	        @PathVariable String category) {

	    List<Product> products =
	            productService.findAllProductByCategory(category);

	    return ResponseEntity.ok(products);
	}

	@GetMapping("/all")
	public ResponseEntity<List<Product>> getAllProduct()
	{
		return ResponseEntity.ok(productService.findAllProduct());
	}
}
