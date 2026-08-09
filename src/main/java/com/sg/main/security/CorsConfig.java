package com.sg.main.security;

import java.util.List;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

@Configuration
public class CorsConfig {

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration config = new CorsConfiguration();

        config.setAllowedOrigins(List.of(
                "http://localhost:3000",   // React dev server (Create React App)
                "http://localhost:5173",   // Vite dev server
                "http://localhost:5500",   // VS Code Live Server default
                "http://127.0.0.1:5500",   // Live Server sometimes uses 127.0.0.1 instead of localhost
                "http://localhost:8081",   // just in case a second backend/frontend uses this
                "null"                     // ONLY for local testing by opening an HTML file directly.
                                            // REMOVE this line before deploying to production - it's
                                            // not a real security boundary and shouldn't ship.
        ));

        config.setAllowedMethods(List.of("GET", "POST", "PUT", "DELETE", "OPTIONS"));
        config.setAllowedHeaders(List.of("Authorization", "Content-Type"));
        config.setAllowCredentials(true);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", config);
        return source;
    }
}