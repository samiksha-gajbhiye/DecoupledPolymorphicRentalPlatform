package com.sg.main.dto;

import com.sg.main.entities.Product;

public record SearchHit(Product product, double score, boolean strong) {}
