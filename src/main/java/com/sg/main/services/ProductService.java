package com.sg.main.services;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Product;
import com.sg.main.entities.ProductImage;
import com.sg.main.repositories.ProductImageRepository;
import com.sg.main.repositories.ProductRepository;

import jakarta.persistence.criteria.Path;

@Service
public class ProductService {

	@Autowired
	private ProductRepository productRepository ;
	@Autowired
	private ProductImageRepository productImageRepository;
	
	
	public Product registerProduct(Product product,
	        List<MultipartFile> productImages) throws IOException {

	    product = productRepository.save(product);

	    String uploadDir = "uploads/products/";

	    File directory = new File(uploadDir);

	    if (!directory.exists()) {
	        directory.mkdirs();
	    }

	    boolean firstImage = true;

	    for (MultipartFile image : productImages) {

	        String fileName = System.currentTimeMillis() + "_"
	                + image.getOriginalFilename();

	        java.nio.file.Path path = Paths.get(uploadDir, fileName);

	        Files.write(path, image.getBytes());

	        ProductImage img = new ProductImage();
 
	        img.setProduct(product);
	        img.setImageUrl(fileName);
	        img.setPrimaryImage(firstImage);

	        firstImage = false;

	        productImageRepository.save(img);
	    }

	    return product;
	}
	
	
}
