import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import HomePage from './pages/HomePage';
import SearchPage from './pages/SearchPage';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import VehicleListPage from './pages/VehicleListPage';  // Importe a página de listagem de veículos
import ReservationPage from './pages/ReservationPage';  // Importe a página de reserva

function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/" exact component={HomePage} />
                    <Route path="/search" component={SearchPage} />
                    <Route path="/login" component={LoginPage} />
                    <Route path="/dashboard" component={Dashboard} />
                    <Route path="/vehicles" component={VehicleListPage} />  {/* Adiciona a rota de listagem de veículos */}
                    <Route path="/reserve/:vehicleID" component={ReservationPage} />  {/* Adiciona a rota de reserva */}
                </Switch>
            </div>
        </Router>
    );
}

export default App;
