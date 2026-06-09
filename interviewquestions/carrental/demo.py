from datetime import date
from .vehicle_rental_system import VehicleRentalSystem
from .store import Store
from .user import User
from .location import Location
from .product.vehicle import Vehicle
from .product.vehicle_type import VehicleType
from .reservation.reservation_type import ReservationType
from .Bill.daily_billing_strategy import DailyBillingStrategy
from .payment.upi_payment_strategy import UPIPaymentStrategy


def main():
    print("\n===== LLD: Car Rental System Demo =====")

    rental_system = VehicleRentalSystem()

    # 1. Create Stores in System
    store1_location = Location(45, "Area1", "City1", "State1", "India", 12345)
    store1 = Store(1001, store1_location)
    rental_system.add_store(store1)

    # 2. Create Users in System
    user1 = User(801, "SJ", "DL2022GDG556690")
    user2 = User(802, "DJ", "DL2017DHW9090765231")
    rental_system.add_user(user1)
    rental_system.add_user(user2)

    # 3. Add vehicles to store inventory
    v1 = Vehicle(1, "DL1234", VehicleType.FOUR_WHEELER)
    v1.set_daily_rental_cost(1100)

    v2 = Vehicle(2, "DL5678", VehicleType.FOUR_WHEELER)
    v2.set_daily_rental_cost(1400)

    store1.get_inventory().add_vehicle(v1)
    store1.get_inventory().add_vehicle(v2)

    # 4. User selects store and searches vehicles
    selected_store = rental_system.get_store(1001)

    from_date = date(2025, 12, 5)
    to_date = date(2025, 12, 7)

    print("\nAvailable vehicles from " + str(from_date) + " to " + str(to_date) + ":")
    for v in selected_store.get_vehicles(VehicleType.FOUR_WHEELER, from_date, to_date):
        print(" - " + str(v.get_vehicle_id()) + ": " + str(v.get_vehicle_type()))

    # 5. User creates reservation
    print("\nCreating reservation...")
    reservation = selected_store.create_reservation(1, user1, from_date, to_date, ReservationType.DAILY)
    print("Reservation created with ID: " + str(reservation.get_reservation_id()))

    # 6. User starts the trip
    print("\nStarting trip...")
    selected_store.start_trip(reservation.get_reservation_id())

    # 7. User submits the vehicle
    print("Submitting vehicle...")
    selected_store.submit_vehicle(reservation.get_reservation_id())

    # 8. System generates the bill
    print("\nGenerating bill...")
    bill = selected_store.generate_bill(reservation.get_reservation_id(),
                                        DailyBillingStrategy(selected_store.get_inventory()))
    print("Bill ID: " + str(bill.get_bill_id()))
    print("Bill Amount: " + str(bill.get_total_bill_amount()))

    # 9. User makes payment
    print("\nProcessing Payment...")
    payment = selected_store.make_payment(bill, UPIPaymentStrategy(), bill.get_total_bill_amount())

    print("\n===== PAYMENT RECEIPT =====")
    print("Payment ID: " + str(payment.get_payment_id()))
    print("Paid Amount: " + str(payment.get_amount_paid()))
    print("Payment Mode: " + str(payment.get_payment_mode()))
    print("Payment Date: " + str(payment.get_payment_date()))
    print("============================")


if __name__ == "__main__":
    main()
