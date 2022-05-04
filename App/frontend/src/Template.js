import React from "react";
import logo from './yelp.png';
import "./Template.css";

function Template() {
  return (
    <header>
      <div className="logo-container">
        <img className="logoImg" src={logo} alt="logo" />
        <h2 className="logo">YELP</h2>


        <div>
        holo
        </div>

      </div>
    

      {/*}
      <nav>
        <div className="nav-links">
          <a className="nav-link" href="#">
            Business Search
          </a>
        </div>
        <div className="nav-links">
          <a className="nav-link" href="#">
            User Information
          </a>
        </div>
      </nav>*/}
    </header>

  );
}

export default Template;
