import React from "react";
import { Nav, Navbar, NavbarBrand, NavItem, Form, FormGroup, Label, Input, FormText } from "reactstrap";
import logo from "../assets/logo.jpg";

const Header: React.FC = () => {
  const containerStyle: React.CSSProperties = {
    position: "relative",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    height: "100px",
  };

  const logoStyle: React.CSSProperties = {
    position: "absolute",
    top: "10px",
    left: "25px",
    width: "150px", // Adjust the width as needed
    height: "auto",
    zIndex: 1, // Ensure the logo stays on top
  };

  const formStyle: React.CSSProperties = {
    backgroundColor: "white",
    padding: "8px",
    borderRadius: "9999px",
    boxShadow: "0px 2px 4px rgba(0, 0, 0, 0.1)", // Add a subtle shadow effect
    zIndex: 0, // Place the form behind the logo
  };

  return (
    <Navbar>
      <div style={containerStyle}>
        <img src={logo} alt="Logo" style={logoStyle} />
        <Form style={formStyle}>
          <FormGroup>
            <Input name="restaurants" placeholder="Search meals, restaurants" />
          </FormGroup>
        </Form>
      </div>
    </Navbar>
  );
};

export default Header;
