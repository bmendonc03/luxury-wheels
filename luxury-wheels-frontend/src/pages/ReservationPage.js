import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

const ReservationPage = ({ match }) => {
    const [customerID, setCustomerID] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [totalPaid, setTotalPaid] = useState('');
    const [status, setStatus] = useState('Reserved');
    const history = useHistory();
    const vehicleID = match.params.vehicleID;

    const handleReservation = (e) => {
        e.preventDefault();

        // Validação: Verificar se a data de início é anterior à data de fim
        if (new Date(startDate) > new Date(endDate)) {
            alert('A data de início não pode ser posterior à data de fim');
            return;
        }

        // Validação: Verificar se os campos obrigatórios estão preenchidos
        if (!customerID || !startDate || !endDate || !totalPaid) {
            alert('Por favor, preencha todos os campos.');
            return;
        }

        const reservationData = {
            vehicle_id: vehicleID,
            customer_id: customerID,
            start_date: startDate,
            end_date: endDate,
            total_paid: totalPaid,
            status: status
        };

        axios.post(`${process.env.REACT_APP_API_URL}/reservations`, reservationData)
            .then(response => {
                alert('Reserva realizada com sucesso!');
                history.push('/');
            })
            .catch(error => {
                console.error('Erro ao fazer reserva:', error);
                alert('Erro ao fazer reserva, tente novamente.');
            });
    };

    return (
        <div className="container">
            <h1 className="my-4">Fazer Reserva</h1>
            <form onSubmit={handleReservation} className="form-group">
                <label>ID do Cliente:</label>
                <input type="text" className="form-control" value={customerID} onChange={(e) => setCustomerID(e.target.value)} required />
    
                <label>Data de Início:</label>
                <input type="date" className="form-control" value={startDate} onChange={(e) => setStartDate(e.target.value)} required />
    
                <label>Data de Fim:</label>
                <input type="date" className="form-control" value={endDate} onChange={(e) => setEndDate(e.target.value)} required />
    
                <label>Total Pago:</label>
                <input type="number" className="form-control" value={totalPaid} onChange={(e) => setTotalPaid(e.target.value)} required />
    
                <button type="submit" className="btn btn-primary mt-3">Confirmar Reserva</button>
            </form>
        </div>
    );    
};

export default ReservationPage;
