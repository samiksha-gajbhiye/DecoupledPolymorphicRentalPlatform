package com.sg.main.dto.python;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record SearchRankData(String query, List<RankedItem> results) {}
