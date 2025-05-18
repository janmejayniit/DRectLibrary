import React, { createContext, useState } from 'react';
import {jwtDecode} from 'jwt-decode';
import {login as loginService } from "../services/userServices.js";

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [authTokens, setAuthTokens] = useState(() => {
    return localStorage.getItem('authTokens') 
      ? JSON.parse(localStorage.getItem('authTokens')) 
      : null;
  });

  const loginUser = async (email, password) => {
    try {
      const data = await loginService(email, password);
      setAuthTokens(data);
      setUser(jwtDecode(data.access));
    } catch (err) {
      console.error('Login failed:', err);
      throw err;
    }
  };


  return (
    <AuthContext.Provider value={{ user, loginUser, authTokens }}>
      {children}
    </AuthContext.Provider>
  );
};
export { AuthProvider, AuthContext };