import React, { Fragment } from "react";
// import "./style.css";
export default function Home() {
  return (
    <div className="p-5">
      <h1 className="text-align-center">Bem vindxs</h1>

      <div className="row">
        <div className="card  min-w-100">
          <div className="card-body">
            <table className="table table-dark">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Mês</th>
                  <th scope="col">Valor</th>
                  <th scope="col">Ações</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>Janeiro</td>
                  <td>R$ 2000 </td>
                  <td>
                    <div className="d-flex  align-items-center  gap-2">
                      <button className="btn btn-primary">Pagar</button>
                      <button className="btn btn-warning">Cortar</button>
                    </div>
                  </td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Jacob</td>
                  <td>Thornton</td>
                  <td>@fat</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Larry</td>
                  <td>the Bird</td>
                  <td>@twitter</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
