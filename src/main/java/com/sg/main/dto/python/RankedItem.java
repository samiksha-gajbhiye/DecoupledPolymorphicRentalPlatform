package com.sg.main.dto.python;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record RankedItem(int id, double score, boolean strong) {}
