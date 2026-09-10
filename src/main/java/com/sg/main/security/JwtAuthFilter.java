package com.sg.main.security;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@Component
public class JwtAuthFilter extends OncePerRequestFilter {

    @Autowired
    private JwtUtil jwtUtil;

    @Autowired
    private UserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(
            HttpServletRequest request,
            HttpServletResponse response,
            FilterChain filterChain)
            throws ServletException, java.io.IOException, java.io.IOException {

        String authHeader = request.getHeader("Authorization");

        String username = null;
        String token = null;

        if (authHeader != null && authHeader.startsWith("Bearer ")) {

            token = authHeader.substring(7);

            try {
                username = jwtUtil.extractUsername(token);
            } catch (Exception e) {
                System.out.println("Invalid JWT token");
            }
        }

        if (username != null &&
        	    SecurityContextHolder.getContext().getAuthentication() == null) {

        	    UserDetails userDetails = null;
        	    try {
        	        userDetails = userDetailsService.loadUserByUsername(username);
        	    } catch (Exception e) {
        	        System.out.println("User from token no longer exists: " + username);
        	    }

        	    if (userDetails != null && jwtUtil.validateToken(token, userDetails.getUsername())) {
        	        UsernamePasswordAuthenticationToken authentication =
        	                new UsernamePasswordAuthenticationToken(
        	                        userDetails,
        	                        null,
        	                        userDetails.getAuthorities()
        	                );
        	        authentication.setDetails(
        	                new WebAuthenticationDetailsSource()
        	                        .buildDetails(request)
        	                );
        	        SecurityContextHolder
        	                .getContext()
        	                .setAuthentication(authentication);
        	    }
        	}

        filterChain.doFilter(request, response);
    }
}