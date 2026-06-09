from .product.vehicle_inventory_manager import VehicleInventoryManager
from .reservation.reservation_manager import ReservationManager
from .Bill.bill_manager import BillManager
from .Bill.daily_billing_strategy import DailyBillingStrategy
from .payment.payment_manager import PaymentManager
from .payment.upi_payment_strategy import UPIPaymentStrategy


class Store:
    def __init__(self, store_id, location):
        self._store_id = store_id
        self._store_location = location
        self._inventory = VehicleInventoryManager()
        self._bill_manager = BillManager(DailyBillingStrategy(self._inventory))
        self._payment_manager = PaymentManager(UPIPaymentStrategy())
        self._reservation_manager = ReservationManager(self._inventory)

    def get_vehicles(self, vehicle_type, from_date, to_date):
        return self._inventory.get_available_vehicles(vehicle_type, from_date, to_date)

    def create_reservation(self, vehicle_id, user, from_date, to_date, reservation_type):
        return self._reservation_manager.create_reservation(vehicle_id, user, from_date, to_date, reservation_type)

    def cancel_reservation(self, reservation_id):
        self._reservation_manager.cancel_reservation(reservation_id)

    def start_trip(self, reservation_id):
        self._reservation_manager.start_trip(reservation_id)

    def submit_vehicle(self, reservation_id):
        self._reservation_manager.submit_vehicle(reservation_id)

    def generate_bill(self, reservation_id, billing_strategy):
        r = self._reservation_manager.find_by_id(reservation_id)
        if r is None:
            raise RuntimeError("Reservation not found")
        self._bill_manager.set_billing_strategy(billing_strategy)
        return self._bill_manager.generate_bill(r)

    def make_payment(self, bill, payment_strategy, payment_amount):
        self._payment_manager.set_payment_strategy(payment_strategy)
        payment = self._payment_manager.make_payment(bill, payment_amount)
        if not bill.is_bill_paid():
            raise RuntimeError("Payment failed")
        self._reservation_manager.remove(bill.get_reservation_id())
        return payment

    def get_inventory(self):
        return self._inventory

    def get_store_id(self):
        return self._store_id
