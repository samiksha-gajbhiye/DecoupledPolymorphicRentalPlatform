package com.sg.main.entities;

import java.math.BigDecimal;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

import org.hibernate.annotations.CreationTimestamp;

import com.sg.main.entities.enums.AvailabilityStatus;
import com.sg.main.entities.enums.ProductCondition;

import jakarta.persistence.CascadeType;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToMany;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import jakarta.persistence.OneToOne;

@Entity
public class Product {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int  productId;
	@ManyToOne
	@JoinColumn(name = "userId")
	private User user ;
	@ManyToOne
	@JoinColumn(name = "categoryId")
	private Category category;
	@Column(nullable = false , length = 30 )
	private String title ;
	@Column(nullable = false , length = 2000)
	private String  description ;
	@Column(nullable = false , length = 50 )
	private String brand;
	@Column(nullable = false , length = 50 )
	private String model ;
	@Column(nullable = false , precision = 10, scale = 3)
	private BigDecimal pricePerDay;
	@Column(unique = true)
	private String productCode;
	private String location;
	@CreationTimestamp
	private LocalDateTime createdAt;
	@CreationTimestamp
	private LocalDateTime updatedAt;
	private boolean verified= false;
	private boolean active =true;
	@Enumerated(EnumType.STRING)
	@Column(name = "product_condition")
	private ProductCondition condition;
	@Column( precision = 10, scale = 3)
	private BigDecimal securityDeposit;
	@Column(nullable = false)
	private int quantity=1;
	
	@Enumerated(EnumType.STRING)
	private AvailabilityStatus availability;
	@OneToMany(
		    mappedBy = "product",
		    cascade = CascadeType.ALL,
		    orphanRemoval = true
		)
		private List<ProductImage> images = new ArrayList<>();
	
	public int getProductId() {
		return productId;
	}
	public void setProductId(int productId) {
		this.productId = productId;
	}
	public User getUser() {
		return user;
	}
	public void setUser(User user) {
		this.user = user;
	}
	public Category getCategory() {
		return category;
	}
	public void setCategory(Category category) {
		this.category = category;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	public String getBrand() {
		return brand;
	}
	public void setBrand(String brand) {
		this.brand = brand;
	}
	public String getModel() {
		return model;
	}
	public void setModel(String model) {
		this.model = model;
	}
	
	public BigDecimal getPricePerDay() {
		return pricePerDay;
	}
	public void setPricePerDay(BigDecimal pricePerDay) {
		this.pricePerDay = pricePerDay;
	}
	public BigDecimal getSecurityDeposit() {
		return securityDeposit;
	}
	public void setSecurityDeposit(BigDecimal securityDeposit) {
		this.securityDeposit = securityDeposit;
	}
	public int getQuantity() {
		return quantity;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	public AvailabilityStatus getAvailability() {
		return availability;
	}
	public void setAvailability(AvailabilityStatus availability) {
		this.availability = availability;
	}
	
	public String getProductCode() {
		return productCode;
	}
	public void setProductCode(String productCode) {
		this.productCode = productCode;
	}
	public String getLocation() {
		return location;
	}
	public void setLocation(String location) {
		this.location = location;
	}
	public LocalDateTime getCreatedAt() {
		return createdAt;
	}
	public void setCreatedAt(LocalDateTime createdAt) {
		this.createdAt = createdAt;
	}
	public LocalDateTime getUpdatedAt() {
		return updatedAt;
	}
	public void setUpdatedAt(LocalDateTime updatedAt) {
		this.updatedAt = updatedAt;
	}
	public boolean isVerified() {
		return verified;
	}
	public void setVerified(boolean verified) {
		this.verified = verified;
	}
	public boolean isActive() {
		return active;
	}
	public void setActive(boolean active) {
		this.active = active;
	}
	
	public ProductCondition getCondition() {
		return condition;
	}
	public void setCondition(ProductCondition condition) {
		this.condition = condition;
	}
	public Product() {
		super();
		// TODO Auto-generated constructor stub
	}
	
	
}
