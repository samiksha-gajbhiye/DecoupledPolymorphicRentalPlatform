package com.sg.main.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.sg.main.entities.ImageVerificationResult;

@Repository
public interface ImageVerificationResultRepository extends JpaRepository<ImageVerificationResult, Integer>{

	ImageVerificationResult save(ImageVerificationResult result);

}
