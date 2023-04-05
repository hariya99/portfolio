// Importing modules
// import React, { useState, useEffect } from "react";
import "./App.css";
// import Test from "./tests/Test";
import { NavBar } from "./components/NavBar";
import Home from "./components/Home";

function App() {
  return (
    <div>
      {/* <Test /> */}
	  <NavBar />
	  <Home />
    </div>
  );
}

export default App;
