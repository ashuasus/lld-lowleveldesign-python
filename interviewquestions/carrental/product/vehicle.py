from .vehicle_status import VehicleStatus


class Vehicle:
    def __init__(self, vehicle_id, vehicle_number, vehicle_type):
        self._vehicle_id = vehicle_id
        self._vehicle_number = vehicle_number
        self._vehicle_type = vehicle_type
        self._daily_rental_cost = 0.0
        self._vehicle_status = VehicleStatus.AVAILABLE

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_vehicle_type(self):
        return self._vehicle_type

    def get_vehicle_status(self):
        return self._vehicle_status

    def get_daily_rental_cost(self):
        return self._daily_rental_cost

    def get_vehicle_number(self):
        return self._vehicle_number

    def set_daily_rental_cost(self, daily_rental_cost):
        self._daily_rental_cost = daily_rental_cost

    def set_status(self, vehicle_status):
        self._vehicle_status = vehicle_status
