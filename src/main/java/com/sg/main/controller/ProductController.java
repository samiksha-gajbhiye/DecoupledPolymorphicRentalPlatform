package com.sg.main.controller;

import java.io.IOException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Product;
import com.sg.main.entities.User;
import com.sg.main.services.ProductService;
import com.sg.main.services.UserService;

@RestController
@RequestMapping("/product")
public class ProductController {

	@Autowired
	private ProductService productService;

	@Autowired
	private UserService userService;

	@PostMapping("/register")
	public Product registerProduct(
	        @RequestPart("product") Product product,
	        @RequestPart("productImages") List<MultipartFile> productImages,
	        Authentication authentication)
	        throws IOException {

		// SECURITY FIX: ignore whatever user/owner the client sent in the JSON body.
		// Always use the logged-in JWT user as the real owner.
		User owner = userService.findByEmail(authentication.getName());
		product.setUser(owner);

		return productService.registerProduct(product, productImages);
	}

	@PostMapping(value = "/add", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
	public Product addProduct(@RequestPart("product") Product product,
			@RequestPart("images") List<MultipartFile> images,
			Authentication authentication) throws IOException {

		// Same fix here - product ownership always comes from the JWT, never from the client.
		User owner = userService.findByEmail(authentication.getName());
		product.setUser(owner);

		return productService.registerProduct(product, images);
	}

	@GetMapping("/title/{title}")
	public ResponseEntity<List<Product>> getProductByTitle(@PathVariable String title) {

		List<Product> product = productService.GetProductDetailsByName(title);
		return ResponseEntity.ok(product);

	}
}