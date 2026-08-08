package com.sg.main.services;

import java.util.concurrent.TimeUnit;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class RedisService {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    // Save data
    public void save(String key, Object value) {
        redisTemplate.opsForValue().set(key, value);
    }

    // Save data with expiry
    public void save(String key, Object value, long time) {
        redisTemplate.opsForValue().set(key, value, time, TimeUnit.MINUTES);
    }

    // Get data
    public Object get(String key) {
        return redisTemplate.opsForValue().get(key);
    }

    // Delete data
    public void delete(String key) {
        redisTemplate.delete(key);
    }

    // Check if key exists
    public boolean exists(String key) {
        return Boolean.TRUE.equals(redisTemplate.hasKey(key));
    }
   
}