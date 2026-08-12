package com.sg.main.repositories;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.sg.main.entities.OrderItem;

public interface OrderItemRepository extends JpaRepository<OrderItem, Integer> {

    // kisi order ke andar ke sare OrdreItem ko find krta hai 
    List<OrderItem> findByOrder_OrderId(int orderId);

    // kisi owner ke product pe aayi sabhi request ko find krega
    // owner apne product pe aayi sari req dekh skta hai
    List<OrderItem> findByProduct_User_Id(int ownerId);

    // Availability check krta hai
    // Pending, Confirmed and Active order ko check karega
    // if product book hoga to availibity busy dikhayega
    @Query("SELECT oi FROM OrderItem oi WHERE oi.product.productId = :productId " +
           "AND oi.order.status IN ('PENDING', 'CONFIRMED', 'ACTIVE') " +
           "AND oi.order.rentalStart <= :endDate AND oi.order.rentalEnd >= :startDate")
    List<OrderItem> findOverlappingOrderItems(
            @Param("productId") int productId,
            @Param("startDate") LocalDate startDate,
            @Param("endDate") LocalDate endDate);
}