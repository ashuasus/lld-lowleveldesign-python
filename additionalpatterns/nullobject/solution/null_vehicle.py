from ..vehicle import Vehicle


class NullVehicle(Vehicle):
    def __init__(self):
        self._model = "Default"
        self._color = "Default"
        self._seating_capacity = 0
        self._fuel_tank_capacity = 0
        self._is_available_for_test_drive = False

    def start(self):
        # Do nothing - silent Vehicle
        print("\n[-] Null Vehicle: start() - do nothing", end="")

    def stop(self):
        # Do nothing - silent Vehicle
        print("\n[-] Null Vehicle: stop() - do nothing")

    # Getters
    def get_seating_capacity(self):
        return self._seating_capacity

    def get_fuel_tank_capacity(self):
        return self._fuel_tank_capacity

    def is_available_for_test_drive(self):
        return self._is_available_for_test_drive
