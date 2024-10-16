from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    transmission = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    daily_rate = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)
    last_review_date = db.Column(db.Date, nullable=True)
    next_review_date = db.Column(db.Date, nullable=True)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    phone_number = db.Column(db.String(50), nullable=True)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    total_paid = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Reserved', 'Cancelled', 'Completed'

    vehicle = db.relationship('Vehicle', backref=db.backref('reservations', lazy=True))
    customer = db.relationship('Customer', backref=db.backref('reservations', lazy=True))

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)  # e.g., 'Credit Card', 'PayPal'

    reservation = db.relationship('Reservation', backref=db.backref('payments', lazy=True))

def init_db():
    db.create_all()

if __name__ == '__main__':
    from main.py import app
    with app.app_context():
        init_db()
