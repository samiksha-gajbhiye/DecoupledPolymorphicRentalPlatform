package com.sg.main.services;

import java.time.LocalDate;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sg.main.entities.Booking;
import com.sg.main.entities.BookingStatus;
import com.sg.main.entities.Product;
import com.sg.main.entities.User;
import com.sg.main.repositories.BookingRepository;

@Service
public class BookingService {

    @Autowired
    private BookingRepository bookingRepo;

    @Autowired
    private ProductService productService;

    
     // timeperiod of renting

    public Booking requestBooking(User renter, int productId, LocalDate startDate, LocalDate endDate) {

        if (startDate == null || endDate == null || startDate.isAfter(endDate)) {
            throw new RuntimeException("Invalid date range: start date must be before end date");
        }

        if (startDate.isBefore(LocalDate.now())) {
            throw new RuntimeException("Cannot book a start date in the past");
        }

        Product product = productService.getProductById(productId);

        if (product.getUser() != null && product.getUser().getId() == renter.getId()) {
            throw new RuntimeException("You cannot book your own product");
        }

        List<Booking> conflicts = bookingRepo.findOverlappingBookings(productId, startDate, endDate);
        if (!conflicts.isEmpty()) {
            throw new RuntimeException("Product is already booked for the selected dates");
        }

        Booking booking = new Booking();
        booking.setRenter(renter);
        booking.setProduct(product);
        booking.setStartDate(startDate);
        booking.setEndDate(endDate);
        booking.setStatus(BookingStatus.PENDING);

        return bookingRepo.save(booking);
    }

    // owner ke request accept karne ke liye . 
    public Booking acceptBooking(int bookingId, User owner) {
        Booking booking = getOwnedBookingOrThrow(bookingId, owner);

        if (booking.getStatus() != BookingStatus.PENDING) {
            throw new RuntimeException("Only pending bookings can be accepted");
        }

        List<Booking> conflicts = bookingRepo.findOverlappingBookings(
                booking.getProduct().getProductId(), booking.getStartDate(), booking.getEndDate());
        conflicts.removeIf(b -> b.getId() == booking.getId());

        boolean alreadyAccepted = conflicts.stream()
                .anyMatch(b -> b.getStatus() == BookingStatus.ACCEPTED);
        if (alreadyAccepted) {
            throw new RuntimeException("Another booking for these dates was already accepted");
        }

        booking.setStatus(BookingStatus.ACCEPTED);
        return bookingRepo.save(booking);
    }

    // owner ko aayi huyi pending request ko delete karne ke liye
    public Booking rejectBooking(int bookingId, User owner) {
        Booking booking = getOwnedBookingOrThrow(bookingId, owner);

        if (booking.getStatus() != BookingStatus.PENDING) {
            throw new RuntimeException("Only pending bookings can be rejected");
        }

        booking.setStatus(BookingStatus.REJECTED);
        return bookingRepo.save(booking);
    }

    // Renter ko booking cancle karni ho to 
    public Booking cancelBooking(int bookingId, User renter) {
        Booking booking = bookingRepo.findById(bookingId)
                .orElseThrow(() -> new RuntimeException("Booking not found: " + bookingId));

        if (booking.getRenter().getId() != renter.getId()) {
            throw new RuntimeException("You can only cancel your own bookings");
        }

        if (booking.getStatus() == BookingStatus.COMPLETED) {
            throw new RuntimeException("Cannot cancel a completed booking");
        }

        booking.setStatus(BookingStatus.CANCELLED);
        return bookingRepo.save(booking);
    }

    public List<Booking> getMyBookings(User renter) {
        return bookingRepo.findByRenter_Id(renter.getId());
    }

    public List<Booking> getIncomingBookings(User owner) {
        return bookingRepo.findByProduct_User_Id(owner.getId());
    }

    private Booking getOwnedBookingOrThrow(int bookingId, User owner) {
        Booking booking = bookingRepo.findById(bookingId)
                .orElseThrow(() -> new RuntimeException("Booking not found: " + bookingId));

        if (booking.getProduct().getUser() == null
                || booking.getProduct().getUser().getId() != owner.getId()) {
            throw new RuntimeException("You do not own the product for this booking");
        }

        return booking;
    }
}