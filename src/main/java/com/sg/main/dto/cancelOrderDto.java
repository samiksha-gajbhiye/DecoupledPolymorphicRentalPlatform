package com.sg.main.dto;

import java.util.UUID;

public class cancelOrderDto {
	private UUID orderCode;
    private String customerCode;

    public UUID getOrderCode() {
        return orderCode;
    }

    public void setOrderCode(UUID orderCode) {
        this.orderCode = orderCode;
    }

    public String getCustomerCode() {
        return customerCode;
    }

    public void setCustomerCode(String customerCode) {
        this.customerCode = customerCode;
    }
}
