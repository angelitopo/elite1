import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/">Home</Link>
      <Link to="/workouts">Workouts</Link>
      <Link to="/profile">Profile</Link>
    </nav>
  );
}

export default Navbar;
