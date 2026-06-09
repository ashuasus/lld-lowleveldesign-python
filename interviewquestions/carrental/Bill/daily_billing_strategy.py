import itertools
from .billing_strategy import BillingStrategy
from .bill import Bill


class DailyBillingStrategy(BillingStrategy):
    _bill_id_counter = itertools.count(5000)

    def __init__(self, vehicle_inventory_manager):
        self.vehicle_inventory_manager = vehicle_inventory_manager

    def generate_bill(self, reservation):
        delta = reservation.get_date_booked_to() - reservation.get_date_booked_from()
        days = delta.days + 1

        vehicle = self.vehicle_inventory_manager.get_vehicle(reservation.get_vehicle_id())
        rate = vehicle.get_daily_rental_cost()
        total = days * rate

        return Bill(next(DailyBillingStrategy._bill_id_counter), reservation.get_reservation_id(), total)
