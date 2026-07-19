package com.sg.main.services;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.UUID;

import javax.imageio.ImageIO;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import com.sg.main.entities.Category;
import com.sg.main.entities.Product;
import com.sg.main.entities.ProductImage;
import com.sg.main.entities.User;
import com.sg.main.repositories.CategoryRepository;
import com.sg.main.repositories.ProductImageRepository;
import com.sg.main.repositories.ProductRepository;
import com.sg.main.repositories.UserRepository;

import jakarta.persistence.criteria.Path;

@Service
public class ProductService {

	@Autowired
	private ProductRepository productRepository ;
	@Autowired
	private ProductImageRepository productImageRepository;
	@Autowired
	private UserRepository userRepository;
	@Autowired
	private CategoryRepository categoryRepository;
	
	
	
	public Product registerProduct(Product product,
	        List<MultipartFile> productImages) throws IOException {

	   
		System.out.println("========== PRODUCT RECEIVED ==========");

		System.out.println(product);

		System.out.println("User object      : " + product.getUser());
		System.out.println("Category object  : " + product.getCategory());

		if (product.getUser() != null) {
		    System.out.println("User ID = " + product.getUser().getId());
		}

		if (product.getCategory() != null) {
		    System.out.println("Category ID = " + product.getCategory().getCategoryId());
		}

	    User user = userRepository.findById(product.getUser().getId())
	            .orElseThrow(() -> new RuntimeException("User not found"));

	    Category category = categoryRepository.findById(product.getCategory().getCategoryId())
	            .orElseThrow(() -> new RuntimeException("Category not found"));

	    product.setUser(user);
	    product.setCategory(category);
	    
	    product = productRepository.save(product);
	    
	    String uploadDir = "uploads/products/";

	    File directory = new File(uploadDir);

	    if (!directory.exists()) {
	        directory.mkdirs();
	    }

	    boolean firstImage = true;
	    int displayOrder = 1;

	    System.out.println("No. of images = " + productImages.size());
	    for (MultipartFile image : productImages) {

	    	System.out.println("Processing : " + image.getOriginalFilename());

	    	String fileName =
	    	        UUID.randomUUID().toString() + "_" + image.getOriginalFilename();
	        java.nio.file.Path path = Paths.get(uploadDir, fileName);

	        Files.write(path, image.getBytes());

	        System.out.println("File Name : " + image.getOriginalFilename());
	        System.out.println("Content Type : " + image.getContentType());
	        System.out.println("Size : " + image.getSize());
	        
	        BufferedImage bufferedImage = ImageIO.read(image.getInputStream());

	        ProductImage img = new ProductImage();

	        img.setProduct(product);
	        img.setImageUrl(fileName);

	        img.setPrimaryImage(firstImage);
	        img.setDisplayOrder(displayOrder++);

	        img.setFileSize(image.getSize());
	        img.setFileType(image.getContentType());

	        img.setWidth(bufferedImage.getWidth());
	        img.setHeight(bufferedImage.getHeight());

	        productImageRepository.save(img);

	        firstImage = false;
	    }

	    return product;
	}
	
	
}
