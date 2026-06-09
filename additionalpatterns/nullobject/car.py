from .vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, model, color, seating_capacity, fuel_tank_capacity, is_available_for_test_drive):
        self._model = model
        self._color = color
        self._seating_capacity = seating_capacity
        self._fuel_tank_capacity = fuel_tank_capacity
        self._is_available_for_test_drive = is_available_for_test_drive

    def start(self):
        print("Car is started and moving")

    def stop(self):
        print("Car is stopped")

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
