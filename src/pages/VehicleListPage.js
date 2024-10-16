import React, { useState, useEffect } from 'react';
import axios from 'axios';

const VehicleListPage = () => {
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        // Faz chamada à API para buscar veículos
        axios.get(`${process.env.REACT_APP_API_URL}/vehicles`)
            .then(response => {
                setVehicles(response.data);
            })
            .catch(error => {
                console.error('Erro ao buscar veículos:', error);
            });
    }, []);

    return (
        <div>
            <h1>Lista de Veículos</h1>
            <div className="vehicle-list">
                {vehicles.map(vehicle => (
                    <div key={vehicle.id} className="vehicle-item">
                        <h3>{vehicle.brand} {vehicle.model}</h3>
                        <p>Categoria: {vehicle.category}</p>
                        <p>Preço diário: {vehicle.daily_rate}</p>
                        <img src={vehicle.image_url} alt={`${vehicle.brand} ${vehicle.model}`} />
                        {/* Adicionar link para fazer reserva */}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default VehicleListPage;
