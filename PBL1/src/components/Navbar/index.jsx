import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand">Consumágua</a>
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item active">
            <Link to="/home" className="nav-link">
              Home
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/history" className="nav-link">
              Histórico de contas
            </Link>
          </li>
          <li className="nav-item">
            <Link to="/" className="nav-link"></Link>
          </li>
          {/* <li className="nav-item">
              <a className="nav-link disabled">Disabled</a>
            </li> */}
        </ul>
      </div>
    </nav>
  );
}
