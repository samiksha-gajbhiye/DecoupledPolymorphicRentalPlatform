package com.sg.main.dto.python;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record SearchRankResponse(boolean success, String message, SearchRankData data) {}
