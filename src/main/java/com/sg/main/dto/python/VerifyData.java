package com.sg.main.dto.python;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;

@JsonIgnoreProperties(ignoreUnknown = true)
public record VerifyData(
        String label,
        String category,
        double confidence,
        @JsonProperty("category_confidence") double categoryConfidence,
        @JsonProperty("is_blurry") boolean blurry,
        @JsonProperty("blur_score") double blurScore
) {}