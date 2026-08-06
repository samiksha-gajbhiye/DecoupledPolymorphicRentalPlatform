package com.sg.main.dto;

public class LoginResponse {

	private String message;
	private String userCode;
	private String role;
	
    public LoginResponse() {}
    
    
	public LoginResponse(String message, String userCode, String role) {
		
		this.message = message;
		this.userCode = userCode;
		this.role = role;
	}
	
	
	public String getMessage() {
		return message;
	}
	
	
	public void setMessage(String message) {
		this.message = message;
	}
	
	
	public String getUserCode() {
		return userCode;
	}
	
	
	public void setUserCode(String userCode) {
		this.userCode = userCode;
	}
	
	
	public String getRole() {
		return role;
	}
	
	
	public void setRole(String role) {
		this.role = role;
	}
	
	
	
}
