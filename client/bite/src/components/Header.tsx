// import React, { useState } from "react";
// import { Navbar, NavbarBrand, Form, Input } from "reactstrap";
// import logo from "../assets/logo.png";
// import profilepic from "../assets/profilepic.png"

// const Header: React.FC = () => {
//   const logoStyle: React.CSSProperties = {
//     height: "30px",
//   };

//   const formStyle: React.CSSProperties = {
//     borderRadius: "9999px",
//     justifyContent: "center",
//     paddingLeft: "20px",
//     alignItems: "center",
//     width: "300px",
//     backgroundColor: "#E5E7EB", // Set the form's background color to grey
//   };

//   const navbarStyle: React.CSSProperties = {
//     borderBottom: "1px solid #D1D5DB", // Add a bottom border to the navbar
//   };

//   const [loggedIn, setLoggedIn] = useState(false); // Set initial login status
//   const [showDropdown, setShowDropdown] = useState(false); // Toggle dropdown visibility

//   const handleLogin = () => {
//     // Handle login logic
//     setLoggedIn(true);
//   };

//   const handleLogout = () => {
//     // Handle logout logic
//     setLoggedIn(false);
//     setShowDropdown(false); // Close dropdown on logout
//   };

//   const handleToggleDropdown = () => {
//     setShowDropdown(!showDropdown); // Toggle dropdown visibility
//   };

//   const dropdownStyle: React.CSSProperties = {
//     width: "200px", // Set the desired width for the dropdown
//   };

//   return (
//     <Navbar light expand="md" className="flex justify-between items-center py-2" style={navbarStyle}>
//       <NavbarBrand href="/" className="text-gray-800 text-lg font-bold">
//         <img src={logo} alt="Logo" style={logoStyle} />
//       </NavbarBrand>
//       <Form inline className="flex-grow">
//         <input
//           name="restaurants"
//           style={formStyle}
//           placeholder="Search foods, restaurants"
//           className="border-gray-400 focus:border-gray-600 focus:border-black rounded-full px-4 py-2 text-sm w-full"
//         />
//       </Form>
//       {loggedIn ? (
//         <div className="relative">
//           <button
//             type="button"
//             className="rounded-full bg-white text-white font-bold text-base px-4 py-2"
//             onClick={handleToggleDropdown}
//           >
//         <img src={profilepic} alt="Account" style={logoStyle} />
//           </button>
//           {showDropdown && (
//             <div className="absolute right-0 mt-2 bg-white rounded-lg shadow-lg py-2" style={dropdownStyle}>
//               <div>
//                 <a href="/" className="text-gray-800 font-semibold no-underline hover:bg-gray-200 block px-4 py-2">
//                   My Account
//                 </a>
//               </div>
//               <div>
//                 <a href="/" className="text-gray-800 font-semibold no-underline hover:bg-gray-200 block px-4 py-2">
//                   Previous Orders
//                 </a>
//               </div>
//               <div>
//                 <a href="/" className="text-gray-800 font-semibold no-underline hover:bg-gray-200 block px-4 py-2">
//                   Help
//                 </a>
//               </div>
//               <div>
//                 <button
//                   type="button"
//                   className="px-4 text-red-500 text-sm bg-white rounded-full  font-semibold py-1 px-4"
//                   onClick={handleLogout}
//                 >
//                   Logout
//                 </button>
//               </div>
//             </div>
//           )}
//         </div>
//       ) : (
//         <button
//           type="button"
//           className="rounded-full bg-red-500 border-red-500 text-white font-bold text-base px-4 py-2"
//           onClick={handleLogin}
//         >
//           Sign In
//         </button>
//       )}
//     </Navbar>
//   );
// };

// export default Header;

import React, { useState } from "react";
import { Navbar, NavbarBrand, Form, Input } from "reactstrap";
import logo from "../assets/logo.png";
import profilepic from "../assets/profilepic.png";

const Header: React.FC = () => {
  const logoStyle: React.CSSProperties = {
    height: "33px",
  };

  const formStyle: React.CSSProperties = {
    borderRadius: "9999px",
    display: "flex",
    justifyContent: "center",
    paddingLeft: "20px",
    alignItems: "center",
    width: "450px",
    backgroundColor: "#E5E7EB", // Set the form's background color to grey
  };

  const navbarStyle: React.CSSProperties = {
    borderBottom: "1px solid #D1D5DB", // Add a bottom border to the navbar
  };

  const [loggedIn, setLoggedIn] = useState(false); // Set initial login status
  const [showDropdown, setShowDropdown] = useState(false); // Toggle dropdown visibility

  const handleLogin = () => {
    // Handle login logic
    setLoggedIn(true);
  };

  const handleLogout = () => {
    // Handle logout logic
    setLoggedIn(false);
    setShowDropdown(false); // Close dropdown on logout
  };

  const handleToggleDropdown = () => {
    setShowDropdown(!showDropdown); // Toggle dropdown visibility
  };

  const dropdownStyle: React.CSSProperties = {
    width: "200px", // Set the desired width for the dropdown
  };

  return (
    <Navbar light expand="md" className="flex justify-between items-center py-2" style={navbarStyle}>
      <NavbarBrand href="/" className="text-gray-800 text-lg font-bold">
        <img src={logo} alt="Logo" style={logoStyle} />
      </NavbarBrand>
      <Form inline className="flex-grow">
        <input
          name="restaurants"
          style={formStyle}
          placeholder="Search foods, restaurants"
          className="border-gray-400 focus:border-gray-600 focus:border-black rounded-full px-4 py-2 text-sm w-full"
        />
      </Form>
      {loggedIn ? (
        <div className="relative">
          <button
            type="button"
            className="rounded-full bg-white text-white font-bold text-base px-4 py-2"
            onClick={handleToggleDropdown}
          >
            <img src={profilepic} alt="Account" style={logoStyle} />
          </button>
          {showDropdown && (
            <div className="absolute right-0 mt-2 bg-white rounded-lg shadow-lg py-2" style={dropdownStyle}>
              <div>
                <a href="/" className="text-gray-800 font-semibold no-underline hover:bg-gray-200 block px-4 py-2">
                  My Account
                </a>
              </div>
              <div>
                <a href="/" className="text-gray-800 font-semibold no-underline hover:bg-gray-200 block px-4 py-2">
                  Previous Orders
                </a>
              </div>
              <div>
                <a href="/" className="text-gray-800 font-semibold no-underline hover:bg-gray-200 block px-4 py-2">
                  Help
                </a>
              </div>
              <div>
                <button
                  type="button"
                  className="px-4 text-red-500 text-sm bg-white rounded-full  font-semibold py-1 px-4"
                  onClick={handleLogout}
                >
                  Logout
                </button>
              </div>
            </div>
          )}
        </div>
      ) : (
        <button
          type="button"
          className="rounded-full bg-red-500 border-red-500 text-white font-bold text-base px-4 py-2"
          onClick={handleLogin}
        >
          Sign In
        </button>
      )}
    </Navbar>
  );
};

export default Header;
