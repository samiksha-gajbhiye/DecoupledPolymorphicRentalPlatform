package com.sg.main.dto.python;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonProperty;

public record SearchRankRequest(
        String query,
        List<SearchItem> items,
        @JsonProperty("top_k") int topK
) {}
