class ParkingLevel:
    def __init__(self, level_number, managers):
        self._level_number = level_number
        self._managers = managers

    def has_availability(self, vehicle_type):
        manager = self._managers.get(vehicle_type)
        return manager is not None and manager.has_free_spot()

    def park(self, vehicle_type):
        manager = self._managers.get(vehicle_type)
        if manager is None:
            raise ValueError("No parking manager for vehicle type: " + str(vehicle_type))
        return manager.park()

    def un_park(self, vehicle_type, spot):
        manager = self._managers.get(vehicle_type)
        if manager is not None:
            manager.un_park(spot)

    def get_level_number(self):
        return self._level_number
