from models.customer import Customer
from models.table import Table
from models.reservation import Reservation
from models.database import session

def main_menu():
    while True:
        print("\nRestaurant Reservation System")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Make a Reservation")
        print("4. View Reservations")
        print("5. Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            view_customers()
        elif choice == "3":
            make_reservation()
        elif choice == "4":
            view_reservations()
        elif choice == "5":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")

    new_customer = Customer(name=name, email=email, phone=phone)
    session.add(new_customer)
    session.commit()
    print(f"Customer {name} added successfully!")

def view_customers():
    customers = session.query(Customer).all()
    if not customers:
        print("No customers found.")
        return
    
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")

def make_reservation():
    customer_id = input("Enter customer ID: ")
    table_number = input("Enter table number: ")
    time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")

    new_reservation = Reservation(customer_id=customer_id, table_number=table_number, time=time)
    session.add(new_reservation)
    session.commit()
    print(f"Reservation made successfully for customer {customer_id} at table {table_number}.")

def view_reservations():
    reservations = session.query(Reservation).all()
    if not reservations:
        print("No reservations found.")
        return
    
    for reservation in reservations:
        print(f"Customer ID: {reservation.customer_id}, Table: {reservation.table_number}, Time: {reservation.time}")
