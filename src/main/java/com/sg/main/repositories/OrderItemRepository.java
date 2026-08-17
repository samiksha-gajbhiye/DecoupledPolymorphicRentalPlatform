package com.sg.main.repositories;

import java.time.LocalDate;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.OrderItem;

import io.lettuce.core.dynamic.annotation.Param;

@Repository
public interface OrderItemRepository extends JpaRepository<OrderItem, Integer> {

	
	@Query("""
		    SELECT oi
		    FROM OrderItem oi
		    WHERE oi.product.productCode = :productCode
		      AND oi.order.status IN ('PENDING', 'CONFIRMED', 'ACTIVE')
		      AND oi.order.rentalStart <= :endDate
		      AND oi.order.rentalEnd >= :startDate
		    """)
		List<OrderItem> findOverLappingOrderItem(
		        @Param("productCode") String productCode,
		        @Param("startDate") LocalDate startDate,
		        @Param("endDate") LocalDate endDate);
			
			
	
	
}
