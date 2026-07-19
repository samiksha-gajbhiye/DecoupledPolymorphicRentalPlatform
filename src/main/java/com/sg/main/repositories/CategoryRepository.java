package com.sg.main.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.Category;

@Repository
public interface CategoryRepository extends JpaRepository<Category, Integer> {

}
