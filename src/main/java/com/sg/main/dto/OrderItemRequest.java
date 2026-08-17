package com.sg.main.dto;

public class OrderItemRequest {

	private String productCode;
	private int quantity;
	public String getProductCode() {
		return productCode;
	}
	public void setProductCode(String productCode) {
		this.productCode = productCode;
	}
	public int getQuantity() {
		return quantity;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}
	@Override
	public String toString() {
		return "OrderItemRequest [productCode=" + productCode + ", quantity=" + quantity + "]";
	}
	
	
	
}
