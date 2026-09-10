import React, { createContext, useContext, useState, useEffect } from 'react';
import { loginRequest, registerRequest } from '../api/authApi';
import { getCurrentUser } from '../api/userApi';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const bootstrap = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        setLoading(false);
        return;
      }
      try {
        const freshUser = await getCurrentUser();
        setUser(freshUser);
        localStorage.setItem('demoRentalUser', JSON.stringify(freshUser));
      } catch (err) {
        setUser(null);
      } finally {
        setLoading(false);
      }
    };
    bootstrap();
  }, []);

  const login = async (email, password) => {
    const data = await loginRequest(email, password);
    localStorage.setItem('token', data.token);
    const fullUser = await getCurrentUser();
    setUser(fullUser);
    localStorage.setItem('demoRentalUser', JSON.stringify(fullUser));
    return fullUser;
  };

  const register = async (userPayload, profileImageFile) => {
    return registerRequest(userPayload, profileImageFile);
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('token');
    localStorage.removeItem('demoRentalUser');
  };

  const updateUser = (userData) => {
    setUser(userData);
    localStorage.setItem('demoRentalUser', JSON.stringify(userData));
  };

  const value = { user, login, register, logout, updateUser, loading, isAuthenticated: !!user };

  if (loading) return <div>Loading...</div>;

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);