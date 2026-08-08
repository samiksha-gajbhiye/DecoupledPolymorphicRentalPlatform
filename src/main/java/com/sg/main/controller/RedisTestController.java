package com.sg.main.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.sg.main.services.RedisService;

@RestController
@RequestMapping("/redis")
public class RedisTestController {

	 @Autowired
	    private RedisService redisService;

	    @PostMapping("/save")
	    public String save() {
	        redisService.save("name", "Kunal");
	        return "Data saved in Redis";
	    }

	    @GetMapping("/get")
	    public Object get() {
	        return redisService.get("name");
	    }

	    @DeleteMapping("/delete")
	    public String delete() {
	        redisService.delete("name");
	        return "Data deleted";
	
}
}
