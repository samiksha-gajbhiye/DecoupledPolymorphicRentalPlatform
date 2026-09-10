package com.sg.main.entities;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import com.sg.main.entities.enums.PaymentStatus;
import com.sg.main.entities.enums.RentalOrderStatus;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToMany;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@Builder
@NoArgsConstructor
@AllArgsConstructor
@Getter
public class RentalOrder {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int orderId;
	@ManyToOne
	@JoinColumn(name = "userId")
	private User customer ;

	@OneToMany(mappedBy = "order")
	private List<Payment> payment;
	private UUID orderCode;
	@CreationTimestamp
	private LocalDate bookingDate;
	@Column(nullable = false )
	private LocalDate rentalStart;
	@Column(nullable = false)
	private LocalDate rentalEnd;
	@Column(nullable = false, precision = 10, scale = 2)
	private BigDecimal subTotal;
	@Column(nullable = false, precision = 10, scale = 2)
	private BigDecimal discount;
	@Column(nullable = false, precision = 10, scale = 2)
	private BigDecimal deposit;
	@Column(nullable = false, precision = 10, scale = 2)
	private BigDecimal grandTotal;
	@Enumerated(EnumType.STRING)
	private RentalOrderStatus status;
	@Enumerated(EnumType.STRING)
	private PaymentStatus paymentStatus;
	private LocalDate actualReturnDate;
	@Column(nullable = false, precision = 10, scale = 2)
	private BigDecimal lateFee;
	@Column(nullable = false)
	private int quantity=1;
	private String paymentTransactionId;
	private String cancellationReason;
	@CreationTimestamp
	private LocalDateTime createdAt;

	@UpdateTimestamp
	private LocalDateTime updatedAt;
	private LocalDateTime cancelledAt;
	private String returnRemarks;
	@Builder.Default
	@OneToMany
	private List<OrderItem> orderItem = new ArrayList<>();

	public int getOrderId() {
		return orderId;
	}
	public void setOrderId(int orderId) {
		this.orderId = orderId;
	}
	public User getCustomer() {
		return customer;
	}
	public void setCustomer(User customer) {
		this.customer = customer;
	}
	public UUID getOrderCode() {
		return orderCode;
	}
	public void setOrderCode(UUID orderCode) {
		this.orderCode = orderCode;
	}
	public LocalDate getBookingDate() {
		return bookingDate;
	}
	public void setBookingDate(LocalDate localDate) {
		this.bookingDate = localDate;
	}
	public LocalDate getRentalStart() {
		return rentalStart;
	}
	public void setRentalStart(LocalDate rentalStart) {
		this.rentalStart = rentalStart;
	}
	public LocalDate getRentalEnd() {
		return rentalEnd;
	}
	public void setRentalEnd(LocalDate rentalEnd) {
		this.rentalEnd = rentalEnd;
	}
	public BigDecimal getSubTotal() {
		return subTotal;
	}
	public void setSubTotal(BigDecimal subTotal) {
		this.subTotal = subTotal;
	}
	public BigDecimal getDiscount() {
		return discount;
	}
	public void setDiscount(BigDecimal discount) {
		this.discount = discount;
	}
	public BigDecimal getDeposit() {
		return deposit;
	}
	public void setDeposit(BigDecimal deposit) {
		this.deposit = deposit;
	}
	public BigDecimal getGrandTotal() {
		return grandTotal;
	}
	public void setGrandTotal(BigDecimal grandTotal) {
		this.grandTotal = grandTotal;
	}
	public RentalOrderStatus getStatus() {
		return status;
	}
	public void setStatus(RentalOrderStatus status) {
		this.status = status;
	}


	public PaymentStatus getPaymentStatus() {
		return paymentStatus;
	}
	public void setPaymentStatus(PaymentStatus paymentStatus) {
		this.paymentStatus = paymentStatus;
	}
	public LocalDate getActualReturnDate() {
		return actualReturnDate;
	}
	public void setActualReturnDate(LocalDate actualReturnDate) {
		this.actualReturnDate = actualReturnDate;
	}
	public BigDecimal getLateFee() {
		return lateFee;
	}
	public void setLateFee(BigDecimal lateFee) {
		this.lateFee = lateFee;
	}
	public int getQuantity() {
		return quantity;
	}
	public void setQuantity(int quantity) {
		this.quantity = quantity;
	}

	public String getPaymentTransactionId() {
		return paymentTransactionId;
	}
	public void setPaymentTransactionId(String paymentTransactionId) {
		this.paymentTransactionId = paymentTransactionId;
	}
	public String getCancellationReason() {
		return cancellationReason;
	}
	public void setCancellationReason(String cancellationReason) {
		this.cancellationReason = cancellationReason;
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

	public LocalDateTime getCancelledAt() {
		return cancelledAt;
	}
	public void setCancelledAt(LocalDateTime cancelledAt) {
		this.cancelledAt = cancelledAt;
	}
	public String getReturnRemarks() {
		return returnRemarks;
	}
	public void setReturnRemarks(String returnRemarks) {
		this.returnRemarks = returnRemarks;
	}


	public List<Payment> getPayment() {
		return payment;
	}
	public void setPayment(List<Payment> payment) {
		this.payment = payment;
	}
	public List<OrderItem> getOrderItem() {
		return orderItem;
	}
	public void setOrderItem(List<OrderItem> orderItem) {
		this.orderItem = orderItem;
	}
	public RentalOrder() {
		super();
		// TODO Auto-generated constructor stub
	}
	@Override
	public String toString() {
		return "RentalOrder [OrderId=" + orderId + ", customer=" + customer + ", OrderCode=" + orderCode
				+ ", bookingDate=" + bookingDate + ", rentalStart=" + rentalStart + ", rentalEnd=" + rentalEnd
				+ ", subTotal=" + subTotal + ", discount=" + discount + ", deposit=" + deposit + ", grandTotal="
				+ grandTotal + ", status=" + status + "]";
	}






}
