package com.sg.main.entities;

import java.math.BigDecimal;
import java.time.LocalDateTime;

import org.hibernate.annotations.CreationTimestamp;

import com.sg.main.entities.enums.PaymentMethod;
import com.sg.main.entities.enums.PaymentStatus;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToOne;



@Entity
public class Payment {
	
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private int paymentId;
@ManyToOne
@JoinColumn(name = "orderId" , unique = true)
private RentalOrder order;
@Enumerated(EnumType.STRING)
private PaymentMethod paymentMethod;
@Column( unique = true)
private String transactionId;
@Column(nullable = false , precision = 20 , scale =  2)
private BigDecimal amount;
@Enumerated(EnumType.STRING)
private PaymentStatus paymentStatus;
@CreationTimestamp
private LocalDateTime paymentDate;

public int getPaymentId() {
	return paymentId;
}
public void setPaymentId(int paymentId) {
	this.paymentId = paymentId;
}
public RentalOrder getOrderId() {
	return order;
}
public void setOrderId(RentalOrder order) {
	this.order = order;
}
public PaymentMethod getPaymentMethod() {
	return paymentMethod;
}
public void setPaymentMethod(PaymentMethod paymentMethod) {
	this.paymentMethod = paymentMethod;
}
public String getTransactionId() {
	return transactionId;
}
public void setTransactionId(String transactionId) {
	this.transactionId = transactionId;
}
public BigDecimal getAmount() {
	return amount;
}
public void setAmount(BigDecimal amount) {
	this.amount = amount;
}
public PaymentStatus getPaymentStatus() {
	return paymentStatus;
}
public void setPaymentStatus(PaymentStatus paymentStatus) {
	this.paymentStatus = paymentStatus;
}
public LocalDateTime getPaymentDate() {
	return paymentDate;
}
public void setPaymentDate(LocalDateTime paymentDate) {
	this.paymentDate = paymentDate;
}
public Payment() {
	super();
	// TODO Auto-generated constructor stub
}
@Override
public String toString() {
	return "Payment [paymentId=" + paymentId + ", orderId=" + order + ", paymentMethod=" + paymentMethod
			+ ", transactionId=" + transactionId + ", amount=" + amount + ", paymentStatus=" + paymentStatus
			+ ", paymentDate=" + paymentDate + "]";
}



}
