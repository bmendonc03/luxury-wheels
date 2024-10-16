from .models import db, Vehicle, Customer, Reservation

def create_vehicle(data):
    new_vehicle = Vehicle(
        brand=data['brand'],
        model=data['model'],
        category=data['category'],
        transmission=data['transmission'],
        type=data['type'],
        daily_rate=data['daily_rate'],
        image_url=data['image_url'],
        last_review_date=data['last_review_date'],
        next_review_date=data['next_review_date']
    )
    db.session.add(new_vehicle)
    db.session.commit()
    return new_vehicle

def get_all_vehicles():
    return Vehicle.query.all()

def create_customer(data):
    new_customer = Customer(
        name=data['name'],
        email=data['email'],
        password_hash=data['password'],  # This should be hashed
        address=data['address'],
        phone_number=data['phone_number']
    )
    db.session.add(new_customer)
    db.session.commit()
    return new_customer

def create_reservation(data):
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
    return new_reservation
