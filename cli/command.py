from sqlalchemy.orm import sessionmaker
from database import engine, get_session
from models import Customer, Reservation  


def create_customer(name, email, phone):
    with get_session() as session:  
        new_customer = Customer(name=name, email=email, phone=phone)
        session.add(new_customer)
        session.commit()


def create_reservation(customer_id, table_id, reservation_time, guests):
    with get_session() as session:
        new_reservation = Reservation(
            customer_id=customer_id,
            table_id=table_id,
            reservation_time=reservation_time,
            guests=guests
        )
        session.add(new_reservation)
        session.commit() 
def get_customers():
    with get_session() as session:
        return session.query(Customer).all()

def get_reservations():
    with get_session() as session:
        return session.query(Reservation).all()

def get_customer_reservations(customer_id):
    with get_session() as session:
        return session.query(Reservation).filter_by(customer_id=customer_id).all()
def update_customer(customer_id, updates):
    with get_session() as session:
        customer = session.query(Customer).filter(Customer.id == customer_id).first()
        if customer:
            if 'name' in updates:
                customer.name = updates['name']
            if 'email' in updates:
                customer.email = updates['email']
            if 'phone' in updates:
                customer.phone = updates['phone']
            session.commit()


def update_reservation(reservation_id, table_id, reservation_time, guests):
    with get_session() as session:
        reservation = session.query(Reservation).filter(Reservation.id == reservation_id).first()
        if reservation:
            reservation.table_id = table_id
            reservation.reservation_time = reservation_time
            reservation.guests = guests
            session.commit()

def delete_customer(customer_id):
    with get_session() as session:
        customer = session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            session.delete(customer)
            session.commit()
            return True
        return False

def delete_reservation(reservation_id):
    with get_session() as session:
        reservation = session.query(Reservation).filter_by(id=reservation_id).first()
        if reservation:
            session.delete(reservation)
            session.commit()
            return True
        return False
