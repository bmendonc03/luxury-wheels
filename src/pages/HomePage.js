import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
    return (
        <div>
            <h1>Bem-vindo à Luxury Wheels</h1>
            <p>Escolha entre uma variedade de veículos de luxo e faça sua reserva online.</p>
            {/* Link para a página de listagem de veículos */}
            <Link to="/vehicles">Ver todos os veículos</Link>
        </div>
    );
};

export default HomePage;
