package com.sg.main.services;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.Optional;
import java.util.UUID;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.PostMapping;

import com.sg.main.dto.ConfirmOrderDto;
import com.sg.main.dto.OrderItemRequest;
import com.sg.main.dto.RentalOrderRequest;
import com.sg.main.dto.cancelOrderDto;
import com.sg.main.entities.OrderItem;
import com.sg.main.entities.Product;
import com.sg.main.entities.RentalOrder;
import com.sg.main.entities.User;
import com.sg.main.entities.enums.RentalOrderStatus;
import com.sg.main.repositories.OrderItemRepository;
import com.sg.main.repositories.ProductRepository;
import com.sg.main.repositories.RentalOrderRepository;
import com.sg.main.repositories.UserRepository;





@Service
public class RentalOrderService {

	
	@Autowired
	private RentalOrderRepository rentalOrderRepo;
	@Autowired
	private OrderItemRepository orderItemRepo;
	@Autowired
	private UserRepository userRepo;
	@Autowired
	private ProductRepository productrepository;

	
	@Transactional
	public RentalOrder createRentalOrder(RentalOrderRequest request) {

	    // =========================
	    // 1. CUSTOMER VALIDATION --> check whether Customer exist krta hai ya nahi 
	    // =========================

	    User customer = userRepo.findByUserCode(request.getCustomerCode())
	            .orElseThrow(() ->
	                    new RuntimeException(
	                            "Customer not found: " + request.getCustomerCode()
	                    )
	            );


	    // =========================
	    // 2. DATE VALIDATION --> check whether dates correct hai ya nahi , koi date past mein toh nahi hai ?
	    //							koi end date start date se pehele toh nahi 
	    //							kahi dates null toh nahi hai 
	    // =========================

	    if (request.getStartDate() == null ||
	        request.getEndDate() == null) {

	        throw new RuntimeException("Rental dates are required");
	    }

	    if (request.getStartDate().isBefore(LocalDate.now())) {

	        throw new RuntimeException(
	                "Rental date cannot be in the past"
	        );
	    }

	    if (request.getEndDate().isBefore(request.getStartDate())) {

	        throw new RuntimeException(
	                "End date cannot be before start date"
	        );
	    }

	    Long rentalDays =
	            ChronoUnit.DAYS.between(
	                    request.getStartDate(),
	                    request.getEndDate()
	            ) + 1;

	    if (rentalDays < 1) {

	        throw new RuntimeException(
	                "Rental days cannot be less than one"
	        );
	    }


	    // =========================
	    // 3. ITEMS VALIDATION --> check whether item empty toh nahi hai 
	    
	    // =========================

	    if (request.getItems() == null ||
	        request.getItems().isEmpty()) {

	        throw new RuntimeException(
	                "At least one product is required"
	        );
	    }


	    // =========================
	    // 4. TOTAL CALCULATIONS--> order k cost sare details calculate karo 
	    // =========================

	    BigDecimal totalSubTotal = BigDecimal.ZERO;
	    BigDecimal totalDeposit = BigDecimal.ZERO;

	    // Store products so we don't query them again later
	    List<Product> products = new java.util.ArrayList<>();


	    // =========================
	    // 5. VALIDATE EACH PRODUCT --> order k har ek item ko validate karo and check karo 
	    //								koi empty value toh pass nahi ho rahi hai 
	    // =========================

	    for (OrderItemRequest itemRequest : request.getItems()) {

	        System.out.println(
	                "SERVICE ITEM = " + itemRequest
	        );

	        System.out.println(
	                "PRODUCT CODE = [" +
	                itemRequest.getProductCode() +
	                "]"
	        );

	        System.out.println(
	                "QUANTITY = [" +
	                itemRequest.getQuantity() +
	                "]"
	        );


	        // Product code validation

	        if (itemRequest.getProductCode() == null ||
	            itemRequest.getProductCode().isBlank()) {

	            throw new RuntimeException(
	                    "Product code is required"
	            );
	        }


	        // Quantity validation

	        if (itemRequest.getQuantity() < 1) {

	            throw new RuntimeException(
	                    "Requested quantity cannot be less than one"
	            );
	        }


	        // Find product

	        Product product =
	                productrepository.findByProductCode(
	                        itemRequest.getProductCode()
	                );


	        System.out.println(
	                "PRODUCT RESULT = " + product
	        );


	        if (product == null) {

	            throw new RuntimeException(
	                    "Product not found: " +
	                    itemRequest.getProductCode()
	            );
	        }


	        // Prevent user renting own product--> user khud ka product khud rent nahi kr skta

	        if (product.getUser() != null &&
	            product.getUser()
	                   .getUserCode()
	                   .equals(request.getCustomerCode())) {

	            throw new RuntimeException(
	                    "You cannot rent your own product"
	            );
	        }


	        // Quantity availability

	        if (itemRequest.getQuantity() >
	            product.getQuantity()) {

	            throw new RuntimeException(
	                    "Requested quantity exceeds available product quantity"
	            );
	        }


	        // Product active validation

	        if (!product.isActive()) {

	            throw new RuntimeException(
	                    "Product is not active"
	            );
	        }


	        // =========================
	        // AVAILABILITY CHECK --> check whether koi rental date already existing rental dates se 
	        //							overlap toh nahi kr rahi hai 
	        // =========================

	        List<OrderItem> overlapping =
	                orderItemRepo.findOverLappingOrderItem(
	                        itemRequest.getProductCode(),
	                        request.getStartDate(),
	                        request.getEndDate()
	                );


	        if (!overlapping.isEmpty()) {

	            throw new RuntimeException(
	                    "Product is already rented for this time period"
	            );
	        }


	        // =========================
	        // PRICE CALCULATION --> total bill calculate karo
	        // =========================

	        BigDecimal pricePerDay =
	                product.getPricePerDay() != null
	                        ? product.getPricePerDay()
	                        : BigDecimal.ZERO;


	        BigDecimal subtotal =
	                pricePerDay
	                        .multiply(BigDecimal.valueOf(rentalDays))
	                        .multiply(
	                                BigDecimal.valueOf(
	                                        itemRequest.getQuantity()
	                                )
	                        );


	        BigDecimal deposit =
	                product.getSecurityDeposit() != null
	                        ? product.getSecurityDeposit()
	                        : BigDecimal.ZERO;


	        totalSubTotal =
	                totalSubTotal.add(subtotal);

	        totalDeposit =
	                totalDeposit.add(deposit);


	        products.add(product);
	    }


	    // =========================
	    // 6. CREATE ONE RENTAL ORDER --> finally rentalOrder mein sare details daal kr order create karo
	    // =========================

	    BigDecimal discount = BigDecimal.ZERO;

	    BigDecimal grandTotal =
	            totalSubTotal
	                    .add(totalDeposit)
	                    .subtract(discount);


	    RentalOrder order = new RentalOrder();

	    order.setCustomer(customer);

	    order.setOrderCode(UUID.randomUUID());

	    order.setRentalStart(
	            request.getStartDate()
	    );

	    order.setRentalEnd(
	            request.getEndDate()
	    );

	    order.setSubTotal(
	            totalSubTotal
	    );

	    order.setDiscount(
	            discount
	    );

	    order.setDeposit(
	            totalDeposit
	    );

	    order.setBookingDate(
	            LocalDate.now()
	    );

	    order.setCreatedAt(
	            LocalDateTime.now()
	    );

	    order.setGrandTotal(
	            grandTotal
	    );

	    order.setLateFee(
	            BigDecimal.ZERO
	    );

	    order.setStatus(
	            RentalOrderStatus.PENDING
	    );


	    order = rentalOrderRepo.save(order);


	    // =========================
	    // 7. CREATE ORDER ITEMS --> 
	    // =========================

	    for (int i = 0; i < request.getItems().size(); i++) {

	        OrderItemRequest itemRequest =
	                request.getItems().get(i);

	        Product product =
	                products.get(i);


	        BigDecimal pricePerDay =
	                product.getPricePerDay() != null
	                        ? product.getPricePerDay()
	                        : BigDecimal.ZERO;


	        BigDecimal subtotal =
	                pricePerDay
	                        .multiply(
	                                BigDecimal.valueOf(rentalDays)
	                        )
	                        .multiply(
	                                BigDecimal.valueOf(
	                                        itemRequest.getQuantity()
	                                )
	                        );


	        OrderItem item = new OrderItem();

	        item.setOrder(order);

	        item.setProduct(product);

	        item.setPricePerDay(
	                pricePerDay
	        );

	        item.setQuantity(
	                itemRequest.getQuantity()
	        );

	        item.setRentalDuration(
	                rentalDays
	        );

	        item.setSubTotal(
	                subtotal
	        );


	        orderItemRepo.save(item);
	    }


	    // =========================
	    // 8. RETURN ORDER
	    // =========================

	    return order;
	}
	
	@Transactional
	public RentalOrder confirmRentalOrder(ConfirmOrderDto confirmOrder) {

	
	//order validation --> check whether order sahi hia ya nahi , kya order exist krta hia 	
	    RentalOrder order = rentalOrderRepo.findByOrderCode(confirmOrder.getOrderCode())
	            .orElseThrow(() ->
	                new RuntimeException("Order not found: " + confirmOrder.getOrderCode())
	            );

	 // check whether order ka status : PENDNING  hia ya nahi 
	    if (order.getStatus() != RentalOrderStatus.PENDING) {
	        throw new RuntimeException(
	            "Only pending orders can be confirmed"
	        );
	    }

	    Product product = order.getOrderItem()
	            .get(0)
	            .getProduct();

	// check whether ye person (owner) actually valide owner hai ya nahi , legitimate owner hi order confirm kr skta hia 
	    if (product.getUser() == null ||
	        !product.getUser().getUserCode().equals(confirmOrder.getOrderCode())) {

	        throw new RuntimeException(
	            "You are not authorized to confirm this order"
	        );
	    }

	// final order confirmation 
	    order.setStatus(RentalOrderStatus.CONFIRMED);

	    return rentalOrderRepo.save(order);
	}
	
	@Transactional
	public RentalOrder cancelRentalOrder(cancelOrderDto cancelOrder) {

	    // 1. Find the order --> kya order exist krta hai 
	    RentalOrder order = rentalOrderRepo.findByOrderCode(cancelOrder.getOrderCode())
	            .orElseThrow(() ->
	                    new RuntimeException("Order not found: " + cancelOrder.getOrderCode())
	            );

	    // 2. Verify that the customer owns this order
	    if (!order.getCustomer().getUserCode().equals(cancelOrder.getCustomerCode())) {
	        throw new RuntimeException(
	                "You cannot cancel someone else's order"
	        );
	    }

	    // 3. Check current status --> only pending ya confirm orders hi cancel ho skte hai 
	    if (order.getStatus() == RentalOrderStatus.CANCELLED) {
	        throw new RuntimeException(
	                "Order is already cancelled"
	        );
	    }

	    if (order.getStatus() == RentalOrderStatus.COMPLETED) {
	        throw new RuntimeException(
	                "Completed orders cannot be cancelled"
	        );
	    }

	    // 4. Change status 
	    order.setStatus(RentalOrderStatus.CANCELLED);

	    // 5. Save
	    return rentalOrderRepo.save(order);
	} 	

}
