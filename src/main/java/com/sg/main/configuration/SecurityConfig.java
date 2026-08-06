package com.sg.main.configuration;

import java.beans.Customizer;
import java.util.List;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

@Configuration
@EnableWebSecurity
public class SecurityConfig {

	 @Bean
	    PasswordEncoder passwordEncoder() {
	        return new BCryptPasswordEncoder();
	    }
	 
	 @Bean
	    SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
		 http
         .csrf(csrf -> csrf.disable())
         .cors(org.springframework.security.config.Customizer.withDefaults())
         .authorizeHttpRequests(auth -> auth
                 .requestMatchers(
                		 "/auth/**",
                		    "/product/all",
                		    "/images/**",
                		    "/error"
                 ).permitAll()
                 .anyRequest().authenticated()
         )
         .formLogin(form -> form.disable())
         .httpBasic(httpBasic -> httpBasic.disable());

     return http.build();
	    } 	
	 
	 @Bean
	    public CorsConfigurationSource corsConfigurationSource() {

	        CorsConfiguration configuration = new CorsConfiguration();

	        configuration.setAllowedOrigins(List.of("http://127.0.0.1:5500"));
	        configuration.setAllowedMethods(List.of("*"));
	        configuration.setAllowedHeaders(List.of("*"));
	        configuration.setAllowCredentials(true);

	        UrlBasedCorsConfigurationSource source =
	                new UrlBasedCorsConfigurationSource();

	        source.registerCorsConfiguration("/**", configuration);

	        return source;
	    }
	
}
