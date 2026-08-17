package com.sg.main.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Product;
import com.sg.main.entities.RentalOrder;
import com.sg.main.entities.User;
import com.sg.main.entities.enums.PaymentStatus;

import java.math.BigDecimal;
import java.util.List;
import java.util.UUID;


@Repository
public interface RentalOrderRepository extends JpaRepository<RentalOrder, Integer> {

	public interface RentalOrderService {

		
		//Create rentalOrder
	    RentalOrder createRentalOrder(RentalOrder order);

	    //Get rentalOrder by 
	    RentalOrder getOrderById(int orderId);
	    
	    

	    RentalOrder getOrderByOrderCode(UUID orderCode);

	    List<RentalOrder> getAllOrders();

	    List<RentalOrder> getOrdersByCustomer(String userCode);

	    List<RentalOrder> getOrdersByOwner(String ownerCode);

	    //Update the rental Order
	    RentalOrder updateOrder(UUID orderCode, RentalOrder order);

	    //cancel the rentalOrder
	    String cancelOrder(UUID orderCode, String reason);

	    //confirm the rental order
	    RentalOrder confirmOrder(UUID orderCode);

	    //reject the rentalOrder
	    RentalOrder rejectOrder(UUID orderCode, String reason);

	    RentalOrder startRental(UUID orderCode);

	    RentalOrder completeRental(UUID orderCode);

	    BigDecimal calculateTotal(UUID orderCode);

	    BigDecimal calculateLateFee(UUID orderCode);

	    RentalOrder updatePaymentStatus(UUID orderCode, PaymentStatus status);

	    String deleteOrder(UUID orderCode);

	}

	public Optional<RentalOrder>  findByOrderCode(UUID orderCode);
	
}
