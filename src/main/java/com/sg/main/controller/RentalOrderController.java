package com.sg.main.controller;

import java.util.UUID;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.dto.OrderItemRequest;
import com.sg.main.dto.RentalOrderRequest;
import com.sg.main.entities.RentalOrder;
import com.sg.main.services.UserService;

@RestController
@RequestMapping("/rentalOrder")
public class RentalOrderController {

	@Autowired
	private com.sg.main.services.RentalOrderService rentalOrderService;
	@Autowired
	private UserService userService;



//order place krne k liye
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

		RentalOrder order = rentalOrderService.createRentalOrder(request, authentication);
		return ResponseEntity.ok(order);

	}


	// order cancel krne  liye
	@PostMapping("/cancelOrder/{orderCode}")
	public ResponseEntity<RentalOrder> cancelOrder(@PathVariable UUID orderCode, Authentication authentication)
	{

		return ResponseEntity.ok(rentalOrderService.cancelRentalOrder(orderCode, authentication));
	}



	//order confirm krne k liya (sirf owner/lender hi order confirm kr skta hai )
	@PostMapping("/confirmOrder/{orderCode}")
	public ResponseEntity<RentalOrder> confirmOrder(@PathVariable UUID orderCode, Authentication authentication)
	{

		return ResponseEntity.ok(rentalOrderService.confirmRentalOrder(orderCode, authentication));
	}


}
