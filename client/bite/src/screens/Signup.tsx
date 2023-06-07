import React, { useState, useEffect } from "react";
import { Navbar, NavbarBrand, Form, Label } from "reactstrap";
import logo from "../assets/logo.png";

const Login: React.FC = () => {
  const logoStyle: React.CSSProperties = {
    height: "33px",
  };

  const formStyle: React.CSSProperties = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    width: "400px",
    borderRadius: "10px",
    padding: "20px",
    margin: "20px auto",
  };

  const labelStyle: React.CSSProperties = {
    marginBottom: "8px",
    fontWeight: "bold",
  };

  const inputStyle: React.CSSProperties = {
    borderRadius: "9999px",
    width: "100%",
    marginBottom: "16px",
    padding: "8px 16px",
    border: "1px solid #D1D5DB",
  };

  const buttonStyle: React.CSSProperties = {
    borderRadius: "9999px",
    backgroundColor: "#EF4444",
    border: "1px solid #EF4444",
    color: "white",
    fontWeight: "bold",
    padding: "8px 16px",
    cursor: "pointer",
  };

  const navbarStyle: React.CSSProperties = {
    borderBottom: "1px solid #D1D5DB",
  };

  const [fadeIn, setFadeIn] = useState(false);

  useEffect(() => {
    setFadeIn(true);
  }, []);

  const fadeInAnimation: React.CSSProperties = {
    opacity: fadeIn ? 1 : 0,
    transition: "opacity 2s ease-in-out",
  };

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // Handle form submission
  };

  return (
    <div>
      <Navbar
        light
        expand="md"
        className="flex justify-between items-center py-2"
        style={navbarStyle}
      >
        <NavbarBrand href="/" className="text-gray-800 text-lg font-bold">
          <img src={logo} alt="Logo" style={logoStyle} />
        </NavbarBrand>
      </Navbar>
      <div style={fadeInAnimation} className= "font-semibold text-gray-800">
        <h6
          style={{
            fontSize: "32px",
            fontWeight: "semi",
            textAlign: "center",
            marginBottom: "20px",
            marginTop:"50px"
          }}
        
        >
          Welcome, Sign Up!
        </h6>
      </div>
      <Form onSubmit={handleSubmit} style={formStyle}>
        <Label htmlFor="username" style={labelStyle} class>
          Enter your username
        </Label>
        <input
          id="username"
          name="username"
          style={inputStyle}
          placeholder="Enter username"
          className="border-gray-400 focus:border-gray-600 focus:border-black rounded-full px-4 py-2 text-sm w-full"
          required
        />

        <Label htmlFor="email" style={labelStyle} >
          Enter your email address
        </Label>
        <input
          id="email"
          name="email"
          style={inputStyle}
          placeholder="Enter email address"
          required
          type="email"
          className="border-gray-400 focus:border-gray-600 focus:border-black rounded-full px-4 py-2 text-sm w-full"

        />

        <Label htmlFor="password" style={labelStyle}>
          Enter your password
        </Label>
        <input
          id="password"
          name="password"
          style={inputStyle}
          placeholder="Enter password"
          type="password"
          className="border-gray-400 focus:border-gray-600 focus:border-black rounded-full px-4 py-2 text-sm w-full"
        />

        <button type="submit" style={buttonStyle}>
          Sign Up
        </button>
      </Form>
      <p style={{ textAlign: "center", marginTop: "16px" }} className="font-semibold">
        Existing user?{" "}
        {/* <Link to="/signup" style={{ color: "#EF4444" }}> */}
          
          <span style={{ color: "#EF4444" }} >Login</span>
        {/* Remember to link the pages together */}
        {/* </Link> */}
      </p>
    </div>
  );
};

export default Login;
