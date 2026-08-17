package com.sg.main.dto;

import java.time.LocalDate;
import java.util.List;

public class RentalOrderRequest {

	private String customerCode;
	private LocalDate startDate;
	private LocalDate endDate;
	private List<OrderItemRequest> items;
	
	public String getCustomerCode() {
		return customerCode;
	}
	public void setCustomerCode(String customerCode) {
		this.customerCode = customerCode;
	}
	public LocalDate getStartDate() {
		return startDate;
	}
	public void setStartDate(LocalDate startDate) {
		this.startDate = startDate;
	}
	public LocalDate getEndDate() {
		return endDate;
	}
	public void setEndDate(LocalDate endDate) {
		this.endDate = endDate;
	}
	
	
	public List<OrderItemRequest> getItems() {
		return items;
	}
	public void setItems(List<OrderItemRequest> items) {
		this.items = items;
	}
	@Override
	public String toString() {
		return "RentalOrderRequest [customerCode=" + customerCode + ", startDate=" + startDate + ", endDate=" + endDate
				+ "]";
	}
	
	
	
	
}
