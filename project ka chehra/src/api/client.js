import axios from 'axios';

export const BASE_URL = 'http://localhost:8080';

const client = axios.create({
  baseURL: BASE_URL,
});

// Runs before every outgoing request — attaches the JWT if we have one
client.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Runs on every response — if the server says 401, the token is dead, log out
client.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('demoRentalUser');
      if (!window.location.pathname.includes('/login')) {
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

export default client;