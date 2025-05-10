import React, { useContext, useState } from 'react';
import { AuthContext } from '../Context/AuthContext';  

// Login component to handle user login
// It uses the AuthContext to access the loginUser function
const Login = () => {
    const { loginUser } = useContext(AuthContext);
    const handleSubmit = e => {
      e.preventDefault();
      loginUser(username, password);
    };
    return (
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Username" onChange={e => setUsername(e.target.value)} />
        <input type="password" placeholder="Password" onChange={e => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
    );
  };
