from ..car import Car
from ..bike import Bike
from .null_vehicle import NullVehicle


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car("Toyota", "Red", 5, 60, True)
        elif vehicle_type == "bike":
            return Bike("Yamaha", "Black", 60)
        else:
            return NullVehicle()  # THE SOLUTION
