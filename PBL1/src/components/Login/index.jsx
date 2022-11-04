import { useState } from "react";
import "./style.css";
export default function Login() {
  const [user, setUser] = useState("");
  const [password, setPassword] = useState("");
  const [isDataValid, setIsDataValid] = useState(false);
  const handleUser = (e) => {
    console.log(e.target.value);
    validateData();
    setUser(e.target.value);
  };
  const handlePassword = (e) => {
    console.log(e.target.value);
    validateData();
    setPassword(e.target.value);
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    let model = {
      user,
      password,
    };
    // TODO Fazer uma requisição de login
  };
  const validateData = () => {
    console.log("JFLKJAKLFAJKLA222");

    if (user.length <= 6 || password.length <= 6) {
      setIsDataValid(false);
    } else {
      setIsDataValid(true);
    }
  };
  return (
    <div className="container">
      <div className="card">
        <div className="card-header">
          <h1>Login</h1>
        </div>
        <div className="card-body">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="user">Usuário</label>
              <input
                type="text"
                id="user"
                value={user}
                onChange={handleUser}
                className="form-control"
              />
            </div>
            <div className="form-group">
              <label htmlFor="password">Senha</label>
              <input
                type="password"
                className="form-control"
                value={password}
                onChange={handlePassword}
                id="password"
              />
            </div>
            <div className="form-group"></div>
            <div className="mt-2">
              <button className="btn btn-danger w-100" disabled={!isDataValid}>
                Logar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}
