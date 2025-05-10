import React, { createContext, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [authTokens, setAuthTokens] = useState(() => {
    return localStorage.getItem('authTokens') 
      ? JSON.parse(localStorage.getItem('authTokens')) 
      : null;
  });

  const loginUser = async (username, password) => {
    const response = await axios.post('/api/users/token/', {
      username,
      password
    });
    if (response.status === 200) {
      setAuthTokens(response.data);
      setUser(jwt_decode(response.data.access));
      localStorage.setItem('authTokens', JSON.stringify(response.data));
    }
  };

  // ... logout, refreshToken, etc.

  return (
    <AuthContext.Provider value={{ user, loginUser, logoutUser, authTokens }}>
      {children}
    </AuthContext.Provider>
  );
};
