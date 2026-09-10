package com.sg.main.entities;

import java.math.BigDecimal;
import java.util.UUID;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
public class OrderItem {

	public long getRentalDuration() {
		return rentalDuration;
	}
	public void setRentalDuration(long rentalDuration) {
		this.rentalDuration = rentalDuration;
	}
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int itemId;

	private UUID orderCode;
	private String productCode;
	@ManyToOne
	@JoinColumn(name = "orderId")
	private RentalOrder order;
	@ManyToOne
	@JoinColumn(name = "productId")
	private Product product;
	@Column(nullable = false )
	private BigDecimal pricePerDay;
	private int quantity=1;
	@Column(nullable = false)
	private BigDecimal subTotal;
	@Column(nullable = false)
	private long rentalDuration;


	public int getItemId() {
		return itemId;
	}
	public void setItemId(int itemId) {
		this.itemId = itemId;
	}
	public RentalOrder getOrder() {
		return order;
	}
	public void setOrder(RentalOrder order) {
		this.order = order;
	}
	public Product getProduct() {
		return product;
	}
	public void setProduct(Product product) {
		this.product = product;
	}
	public BigDecimal getPricePerDay() {
		return pricePerDay;
	}
	public void setPricePerDay(BigDecimal pricePerDay) {
		this.pricePerDay = pricePerDay;
	}
	public int getQuantity(int quantity) {
		return quantity;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	public BigDecimal getSubTotal() {
		return subTotal;
	}
	public void setSubTotal(BigDecimal subTotal) {
		this.subTotal = subTotal;
	}

	public UUID getOrderCode() {
		return orderCode;
	}
	public void setOrderCode(UUID orderCode) {
		this.orderCode = orderCode;
	}

	public String getProductCode() {
		return productCode;
	}
	public void setProductCode(String productCode) {
		this.productCode = productCode;
	}
	public OrderItem() {
		super();
		// TODO Auto-generated constructor stub
	}
	@Override
	public String toString() {
		return "OrderItem [itemId=" + itemId + ", order=" + order + ", product=" + product + ", pricePerDay="
				+ pricePerDay + ", quantity=" + quantity + ", subTotal=" + subTotal + "]";
	}


}
