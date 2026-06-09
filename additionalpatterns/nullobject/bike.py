from .vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self, model, color, fuel_tank_capacity):
        self._model = model
        self._color = color
        self._fuel_tank_capacity = fuel_tank_capacity
        self._is_available_for_test_drive = False
        self._seating_capacity = 2

    def start(self):
        print("Bike is started and moving")

    def stop(self):
        print("Bike is stopped")

    # Getters
    def get_model(self):
        return self._model

    def get_color(self):
        return self._color

    def get_seating_capacity(self):
        return self._seating_capacity

    def get_fuel_tank_capacity(self):
        return self._fuel_tank_capacity

    def is_available_for_test_drive(self):
        return self._is_available_for_test_drive
