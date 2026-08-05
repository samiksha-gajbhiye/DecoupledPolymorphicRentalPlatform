package com.sg.main.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.security.JwtUtil;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/auth")
public class AuthController {

    @Autowired
    private AuthenticationManager authenticationManager;

    @Autowired
    private JwtUtil jwtUtil;

    // Simple request/response DTOs, adjust field names to your liking
    public static class LoginRequest {
        public String username;
        public String password;
    }

    public static class LoginResponse {
        public String token;
        public LoginResponse(String token) { this.token = token; }
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest request) {

        try {
            authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(request.username, request.password));
        } catch (Exception e) {
            // TEMPORARY: print the real cause to console for debugging.
            // Remove this before shipping - don't leak exception details to the client in production.
            e.printStackTrace();
            return ResponseEntity.status(401).body("Auth failed: " + e.getClass().getSimpleName() + " - " + e.getMessage());
        }

        String token = jwtUtil.generateToken(request.username);
        return ResponseEntity.ok(new LoginResponse(token));
    }
}