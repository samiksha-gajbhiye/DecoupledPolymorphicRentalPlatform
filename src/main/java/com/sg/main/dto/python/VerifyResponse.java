package com.sg.main.dto.python;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public record VerifyResponse(boolean success, String message, VerifyData data) {}