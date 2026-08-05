package com.sg.main.exception;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<Map<String, String>> handleRuntimeException(RuntimeException e) {
        return buildResponse(HttpStatus.BAD_REQUEST, e.getMessage());
    }

    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<Map<String, String>> handleAccessDenied(AccessDeniedException e) {
        return buildResponse(HttpStatus.FORBIDDEN, "You do not have permission to perform this action");
    }

    // Catch-all for anything unexpected - never leak the raw stack trace to the client
    @ExceptionHandler(Exception.class)
    public ResponseEntity<Map<String, String>> handleGenericException(Exception e) {
        e.printStackTrace(); // still log the real error server-side for debugging
        return buildResponse(HttpStatus.INTERNAL_SERVER_ERROR, "Something went wrong. Please try again.");
    }

    private ResponseEntity<Map<String, String>> buildResponse(HttpStatus status, String message) {
        Map<String, String> body = new HashMap<>();
        body.put("error", message);
        body.put("status", String.valueOf(status.value()));
        return ResponseEntity.status(status).body(body);
    }
}