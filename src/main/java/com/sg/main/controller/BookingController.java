package com.sg.main.controller;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.entities.Booking;
import com.sg.main.entities.User;
import com.sg.main.services.BookingService;
import com.sg.main.services.UserService;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/booking")
public class BookingController {

    @Autowired
    private BookingService bookingService;

    @Autowired
    private UserService userService; 

    // DTO incoming booking ki body ke liye 
    public static class BookingRequestDto {
        public int productId;
        public LocalDate startDate;
        public LocalDate endDate;
    }

    // renter ko if koi product rent pe lene ke liye req. bhejni ho to 
    @PostMapping("/request")
    public ResponseEntity<?> requestBooking(@RequestBody BookingRequestDto dto, Authentication authentication) {
        try {
            User renter = userService.findByEmail(authentication.getName());
            Booking booking = bookingService.requestBooking(renter, dto.productId, dto.startDate, dto.endDate);
            return ResponseEntity.ok(booking);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // owner ne pending req accept ki tb 
    @PostMapping("/{bookingId}/accept")
    public ResponseEntity<?> acceptBooking(@PathVariable int bookingId, Authentication authentication) {
        try {
            User owner = userService.findByEmail(authentication.getName());
            Booking booking = bookingService.acceptBooking(bookingId, owner);
            return ResponseEntity.ok(booking);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // Owner ne if pending req reject ki tb
    @PostMapping("/{bookingId}/reject")
    public ResponseEntity<?> rejectBooking(@PathVariable int bookingId, Authentication authentication) {
        try {
            User owner = userService.findByEmail(authentication.getName());
            Booking booking = bookingService.rejectBooking(bookingId, owner);
            return ResponseEntity.ok(booking);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // renter ne uski booking cancle ki tb
    @PostMapping("/{bookingId}/cancel")
    public ResponseEntity<?> cancelBooking(@PathVariable int bookingId, Authentication authentication) {
        try {
            User renter = userService.findByEmail(authentication.getName());
            Booking booking = bookingService.cancelBooking(bookingId, renter);
            return ResponseEntity.ok(booking);
        } catch (RuntimeException e) {
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // renter ki sari booking jo usne ki hai 
    @GetMapping("/my-bookings")
    public ResponseEntity<List<Booking>> myBookings(Authentication authentication) {
        User renter = userService.findByEmail(authentication.getName());
        return ResponseEntity.ok(bookingService.getMyBookings(renter));
    }

    // owner ko aayi huyi sari rental req 
    @GetMapping("/incoming")
    public ResponseEntity<List<Booking>> incomingBookings(Authentication authentication) {
        User owner = userService.findByEmail(authentication.getName());
        return ResponseEntity.ok(bookingService.getIncomingBookings(owner));
    }
}