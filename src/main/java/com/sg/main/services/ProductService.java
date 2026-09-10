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
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.security.core.Authentication;
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





	// Method to register product

	@CacheEvict(value = "products", key = "'all'")
	public Product registerProduct(Product product,
	        List<MultipartFile> productImages, Authentication authentication) throws IOException {


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

		//lambda expression to check does user exist or not (true get id or throw runtime exception)

	    User user = userRepository.findByEmail(authentication.getName())
	            .orElseThrow(() -> new RuntimeException("User not found"));

	    //lambda expression to check , does category exist or not (if true get id or throw runtime exception )

	    Category category = categoryRepository.findById(product.getCategory().getCategoryId())
	            .orElseThrow(() -> new RuntimeException("Category not found"));

	    product.setUser(user);
	    product.setCategory(category);


	    // creating automated product code for each category
	    		String prefix = category.getName()
                .substring(0, 3)
                .toUpperCase();

	    		String productCode = prefix + "-"
	    			+ System.currentTimeMillis();

product.setProductCode(productCode);

	    product = productRepository.save(product);


	//uploading the file to local folder

	    String uploadDir = "uploads/products/";

	    File directory = new File(uploadDir);

	    if (!directory.exists()) {
	        directory.mkdirs();
	    }

	    boolean firstImage = true;
	    int displayOrder = 1;

	  //  System.out.println("No. of images = " + productImages.size());


	    //loop to process the product image
	    for (MultipartFile image : productImages) {

	   // 	System.out.println("Processing : " + image.getOriginalFilename());

	    	String fileName =
	    	        UUID.randomUUID().toString() + "_" + image.getOriginalFilename();
	        java.nio.file.Path path = Paths.get(uploadDir, fileName);

	        Files.write(path, image.getBytes());

	      /*  System.out.println("File Name : " + image.getOriginalFilename());
	        System.out.println("Content Type : " + image.getContentType());
	        System.out.println("Size : " + image.getSize());

	       */


	        BufferedImage bufferedImage = ImageIO.read(image.getInputStream());

	        ProductImage img = new ProductImage();


	  // sending the all the data to the database

	        img.setProduct(product);
	        img.setImageUrl("/uploads/products/"+fileName);

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


	//Method to get product

	public List<Product> GetProductDetailsByName(String title )
	{

		return productRepository.findByTitleIgnoreCase(title) ;
	}

	public List<Product> findAllProductByCategory(String categoryName) {

	    if (!productRepository.existsByCategory_Name(categoryName)) {
	        throw new RuntimeException("No product exist in this category yet");
	    }

	    return productRepository.findByCategory_Name(categoryName);
	}


	public Product findProductByProductCode(String productCode) {
		// TODO Auto-generated method stub
		return productRepository.findByProductCode(productCode);
	}

	@Cacheable(value="products",key ="'all'")
	public List<Product> findAllProduct()
	{
		System.out.println("=================================================");
	    System.out.println(">>> EXECUTION HIT DATABASE: Fetching All Products");
	    System.out.println("=================================================");
		return productRepository.findAll();
	}




}
