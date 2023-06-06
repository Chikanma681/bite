import React from "react";
import { Navbar, NavbarBrand, Form, Input } from "reactstrap";
import logo from "../assets/logo.png";

const Header: React.FC = () => {
  const logoStyle: React.CSSProperties = {
    height: "42px",
  };

  const formStyle: React.CSSProperties = {
    borderRadius: "9999px",
    justifyContent: "center",
    paddingLeft: "20px",
    alignItems: "center",
    width: "300px",
    backgroundColor: "#E5E7EB", // Set the form's background color to grey
  };

  const navbarStyle: React.CSSProperties = {
    borderBottom: "1px solid #D1D5DB", // Add a bottom border to the navbar
  };

  return (
    <Navbar light expand="md" className="flex justify-between items-center py-2" style={navbarStyle}>
      <NavbarBrand href="/" className="text-gray-800 text-lg font-bold"><img src={logo} alt="Logo" style={logoStyle} /></NavbarBrand>
      <Form inline className="flex items-center">
        <input
          name="restaurants"
          style={formStyle}
          placeholder="Search foods, restaurants"
          className="border-gray-400 focus:border-gray-600 focus:border-black rounded-full px-4 py-2 text-sm w-full"
        />
      </Form>
      <button
        type="button"
        className="rounded-full bg-red-500 border-red-500 text-white font-bold text-base px-4 py-2"
      >
        Sign In
      </button>
    </Navbar>
  );
};

export default Header;
