package com.sg.main.repositories;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;

import com.sg.main.entities.RentalOrder;

public interface RentalOrderRepository extends JpaRepository<RentalOrder, Integer> {

    // sare orders 
    List<RentalOrder> findByCustomer_Id(int customerId);
}