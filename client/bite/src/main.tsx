import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "typeface-nunito";
import 'tailwindcss/tailwind.css';
import "./index.css";
import "bootstrap/dist/css/bootstrap.css";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
