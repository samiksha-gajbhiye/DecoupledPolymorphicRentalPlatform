package com.sg.main.dto;

import java.util.UUID;

public class ConfirmOrderDto {

	private UUID orderCode;
	private String ownerCode;
	public UUID getOrderCode() {
		return orderCode;
	}
	public void setOrderCode(UUID orderCode) {
		this.orderCode = orderCode;
	}
	public String getOwnerCode() {
		return ownerCode;
	}
	public void setOwnerCode(String ownerCode) {
		this.ownerCode = ownerCode;
	}
	
}
