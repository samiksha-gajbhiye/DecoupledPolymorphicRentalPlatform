package com.sg.main.controller;

import java.util.Optional;
import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.dto.ConfirmOrderDto;
import com.sg.main.dto.OrderItemRequest;
import com.sg.main.dto.RentalOrderRequest;
import com.sg.main.dto.cancelOrderDto;
import com.sg.main.entities.RentalOrder;
import com.sg.main.entities.User;
import com.sg.main.services.UserService;



@RestController
@RequestMapping("/rentalOrder")
public class RentalOrderController {

	@Autowired 
	private com.sg.main.services.RentalOrderService rentalOrderService;
	@Autowired
	private UserService userService;
	
	
	

	@PostMapping("/orderRequest")
	public ResponseEntity<RentalOrder> createRentalOrder(@RequestBody RentalOrderRequest request, Authentication authentication)
	{
		 System.out.println("CUSTOMER = [" + request.getCustomerCode() + "]");
		    System.out.println("START = [" + request.getStartDate() + "]");
		    System.out.println("END = [" + request.getEndDate() + "]");
		    System.out.println("ITEMS = [" + request.getItems() + "]");

		    for (OrderItemRequest item1 : request.getItems()) {

		        System.out.println("ITEM OBJECT = " + item1);
		        System.out.println("PRODUCT CODE = [" + item1.getProductCode() + "]");
		        System.out.println("QUANTITY = [" + item1.getQuantity() + "]");
		    }
		Optional<User> customer = userService.findUser(authentication.getName());
		RentalOrder order = rentalOrderService.createRentalOrder(request);
		return ResponseEntity.ok(order);
		
	}
	
	@PostMapping("/cancelOrder")
	public ResponseEntity<RentalOrder> cancelOrder(@RequestBody cancelOrderDto cancelOrder, Authentication authentication)
	{
		Optional<User> customer = userService.findUser(authentication.getName());
		return ResponseEntity.ok(rentalOrderService.cancelRentalOrder(cancelOrder));
	}
	
	@PostMapping("/confirmOrder")
	public ResponseEntity<RentalOrder> confirmOrder(@RequestBody ConfirmOrderDto confirmOrder , Authentication authentication)
	{
		Optional<User> customer = userService.findUser(authentication.getName());
		return ResponseEntity.ok(rentalOrderService.confirmRentalOrder(confirmOrder));
	}
	

}
