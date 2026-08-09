package com.sg.main.repositories;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.sg.main.entities.Booking;

public interface BookingRepository extends JpaRepository<Booking, Integer> {

    // Renter ne kitni booking ki hai 
    List<Booking> findByRenter_Id(int renterId);

    // owner ke product ki sari booking 
    List<Booking> findByProduct_User_Id(int ownerId);

    // product ki all bookings 
    List<Booking> findByProduct_ProductId(int productId);

    // check ki product ki booking already hai ya nahi if hai to dusri booking ko cancle karo ya avoid second booking
    @Query("SELECT b FROM Booking b WHERE b.product.productId = :productId " +
           "AND b.status IN ('PENDING', 'ACCEPTED') " +
           "AND b.startDate <= :endDate AND b.endDate >= :startDate")
    List<Booking> findOverlappingBookings(
            @Param("productId") int productId,
            @Param("startDate") LocalDate startDate,
            @Param("endDate") LocalDate endDate);
}