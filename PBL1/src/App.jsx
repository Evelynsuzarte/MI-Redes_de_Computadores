import { useState } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import Router from "./routes/Router";
import "./App.css";
import { BrowserRouter } from "react-router-dom";
function App() {
  const [count, setCount] = useState(0);

  return (
    <BrowserRouter>
      <div className="App">
        <Navbar />
        <div className="container">
          <Router />
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
