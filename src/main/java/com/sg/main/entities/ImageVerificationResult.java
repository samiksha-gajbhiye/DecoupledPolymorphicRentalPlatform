package com.sg.main.entities;

import java.time.LocalDateTime;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;

@Entity
public class ImageVerificationResult {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int id ;
	
	@ManyToOne
	@JoinColumn(name="product_image_id" , nullable= false)
	private ProductImage productImage;
	private String label;
	private String category;
	private double confidence;
	private double categoryConfidence;
	private Boolean blurry;
	private double blurryScore;
	private Boolean passed;
	private LocalDateTime checkedAt= LocalDateTime.now();
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public ProductImage getProductImage() {
		return productImage;
	}
	public void setProductImage(ProductImage productImage) {
		this.productImage = productImage;
	}
	public String getLabel() {
		return label;
	}
	public void setLabel(String label) {
		this.label = label;
	}
	public String getCategory() {
		return category;
	}
	public void setCategory(String category) {
		this.category = category;
	}
	public double getConfidence() {
		return confidence;
	}
	public void setConfidence(double confidence) {
		this.confidence = confidence;
	}
	public double getCategoryConfidence() {
		return categoryConfidence;
	}
	public void setCategoryConfidence(double categoryConfidence) {
		this.categoryConfidence = categoryConfidence;
	}
	public Boolean getBlurry() {
		return blurry;
	}
	public void setBlurry(Boolean blurry) {
		this.blurry = blurry;
	}
	public double getBlurryScore() {
		return blurryScore;
	}
	public void setBlurryScore(double blurryScore) {
		this.blurryScore = blurryScore;
	}
	public Boolean getPassed() {
		return passed;
	}
	public void setPassed(Boolean passed) {
		this.passed = passed;
	}
	public LocalDateTime getCheckedAt() {
		return checkedAt;
	}
	public void setCheckedAt(LocalDateTime checkedAt) {
		this.checkedAt = checkedAt;
	}
	public ImageVerificationResult() {
		super();
		// TODO Auto-generated constructor stub
	}
	public ImageVerificationResult(int id, ProductImage productImage, String label, String category, double confidence,
			double categoryConfidence, Boolean blurry, double blurryScore, Boolean passed, LocalDateTime checkedAt) {
		super();
		this.id = id;
		this.productImage = productImage;
		this.label = label;
		this.category = category;
		this.confidence = confidence;
		this.categoryConfidence = categoryConfidence;
		this.blurry = blurry;
		this.blurryScore = blurryScore;
		this.passed = passed;
		this.checkedAt = checkedAt;
	}
	@Override
	public String toString() {
		return "ImageVerficationResult [id=" + id + ", productImage=" + productImage + ", label=" + label
				+ ", category=" + category + ", confidence=" + confidence + ", categoryConfidence=" + categoryConfidence
				+ ", blurry=" + blurry + ", blurryScore=" + blurryScore + ", passed=" + passed + ", checkedAt="
				+ checkedAt + "]";
	}
	
	
	
	
	
}
