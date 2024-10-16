from flask import Blueprint, request, jsonify
from .models import db, Reservation

api = Blueprint('api', __name__)

# Rota para criar uma nova reserva
@api.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    
    try:
        # Criar uma nova reserva
        new_reservation = Reservation(
            vehicle_id=data['vehicle_id'],
            customer_id=data['customer_id'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            total_paid=data['total_paid'],
            status=data['status']
        )
        db.session.add(new_reservation)
        db.session.commit()
        
        return jsonify({"message": "Reserva criada com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
