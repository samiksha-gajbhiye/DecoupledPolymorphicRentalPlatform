package com.sg.main.controller;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.entities.RentalOrder;
import com.sg.main.entities.User;
import com.sg.main.services.RentalOrderService;
import com.sg.main.services.UserService;

@RestController
@RequestMapping("/rental")
public class RentalOrderController {

    @Autowired
    private RentalOrderService rentalOrderService;

    @Autowired
    private UserService userService;

    public static class RentalRequestDto {
        public int productId;
        public LocalDate startDate;
        public LocalDate endDate;
        public int quantity = 1;
    }

    public static class CancelRequestDto {
        public String reason;
    }

    // Renter requests karega product rent pe lene ke liye
    @PostMapping("/request")
    public ResponseEntity<?> requestRental(@RequestBody RentalRequestDto dto, Authentication authentication) {
        try {
            User customer = userService.findByEmail(authentication.getName());
            RentalOrder order = rentalOrderService.requestRental(
                    customer, dto.productId, dto.startDate, dto.endDate, dto.quantity);
            return ResponseEntity.ok(order);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // Owner confirms karega pending req ko
    @PostMapping("/{orderId}/confirm")
    public ResponseEntity<?> confirmOrder(@PathVariable int orderId, Authentication authentication) {
        try {
            User owner = userService.findByEmail(authentication.getName());
            RentalOrder order = rentalOrderService.confirmOrder(orderId, owner);
            return ResponseEntity.ok(order);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // Owner req reject kare ya renter order cancle kare dono yehi se manage honge
    @PostMapping("/{orderId}/cancel")
    public ResponseEntity<?> cancelOrder(@PathVariable int orderId, @RequestBody CancelRequestDto dto, Authentication authentication) {
        try {
            User user = userService.findByEmail(authentication.getName());
            RentalOrder order = rentalOrderService.cancelOrder(orderId, user, dto.reason);
            return ResponseEntity.ok(order);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // Customer ke sare place kiye huye orders
    @GetMapping("/my-orders")
    public ResponseEntity<List<RentalOrder>> myOrders(Authentication authentication) {
        User customer = userService.findByEmail(authentication.getName());
        return ResponseEntity.ok(rentalOrderService.getMyOrders(customer));
    }

    // Owner ko sari product pe aayi huyi req dekhne ke liye
    @GetMapping("/incoming")
    public ResponseEntity<List<RentalOrder>> incomingOrders(Authentication authentication) {
        User owner = userService.findByEmail(authentication.getName());
        return ResponseEntity.ok(rentalOrderService.getIncomingOrders(owner));
    }
}