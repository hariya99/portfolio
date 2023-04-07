// Importing modules
// import React, { useState, useEffect } from "react";
import "./App.css";
// import Test from "./tests/Test";
import { NavBar } from "./components/NavBar";
import Home from "./components/Home";
import {About} from "./components/About";
import Portfolio from "./components/Portfolio";
import GetHome from './Utils'

function App() {
  const data = GetHome("/home")
  return (
    <div>
      {/* <Test /> */}
	  <NavBar />
	  <Home firstName={data.firstName} lastName={data.lastName} intro={data.intro} />
    <About about={data.about} />
    <Portfolio portfolios={data.portfolios} />
    </div>
  );
}

export default App;
