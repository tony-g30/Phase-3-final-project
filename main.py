from cli.command import (
    create_customer,
    create_reservation,
    get_customers,
    get_reservations,
    update_customer,
    delete_customer,
    update_reservation,
    delete_reservation
)

def display_menu():
    print("\n--- Restaurant Reservation System ---")
    print("1. Create Customer")
    print("2. Create Reservation")
    print("3. View Customers")
    print("4. View Reservations")
    print("5. Update Customer")
    print("6. Update Reservation")
    print("7. Delete Customer")
    print("8. Delete Reservation")
    print("9. Exit")

def main_menu():
    while True:
        display_menu()
        choice = input("Select an option (1-9): ")

        if choice == '1':
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            phone = input("Enter customer phone: ")
            create_customer(name, email, phone)
            print("Customer created successfully!")

        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            table_id = input("Enter table ID: ")
            reservation_time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")
            guests = int(input("Enter number of guests: "))
            create_reservation(customer_id, table_id, reservation_time, guests)
            print("Reservation created successfully!")

        elif choice == '3':
            customers = get_customers()
            print("Customers:")
            for customer in customers:
                print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

        elif choice == '4':
            reservations = get_reservations()
            print("Reservations:")
            for reservation in reservations:
                print(f"ID: {reservation.id}, Customer ID: {reservation.customer_id}, Table ID: {reservation.table_id}, Time: {reservation.reservation_time}, Guests: {reservation.guests}")

        elif choice == '5':
            customer_id = input("Enter customer ID to update: ")
            new_name = input("Enter new customer name: ")
            new_email = input("Enter new customer email: ")
            new_phone = input("Enter new customer phone: ")
            update_customer(customer_id, {
                'name': new_name,
                'email': new_email,
               'phone': new_phone
            })          
            print("Customer updated successfully!")

        elif choice == '6':
            reservation_id = int(input("Enter reservation ID to update: "))
            new_table_id = int(input("Enter new table ID: "))
            new_reservation_time = input("Enter new reservation time: ")
            new_guests = int(input("Enter new number of guests: "))
            update_reservation(reservation_id, new_table_id, new_reservation_time, new_guests)
            print("Reservation updated successfully!")

        elif choice == '7':
            customer_id = input("Enter customer ID to delete: ")
            delete_customer(customer_id)
            print("Customer deleted successfully!")

        elif choice == '8':
            reservation_id = input("Enter reservation ID to delete: ")
            delete_reservation(reservation_id)
            print("Reservation deleted successfully!")

        elif choice == '9':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
