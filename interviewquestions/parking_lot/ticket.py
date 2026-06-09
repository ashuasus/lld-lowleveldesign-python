from datetime import datetime


class Ticket:
    def __init__(self, vehicle, level, spot):
        self._vehicle = vehicle
        self._level = level
        self._spot = spot
        self._entry_time = datetime.now()

    def get_vehicle(self):
        return self._vehicle

    def get_level(self):
        return self._level

    def get_spot(self):
        return self._spot

    def get_entry_time(self):
        return self._entry_time
