class ParkingSpot:
    def __init__(self, spot_id):
        self._spot_id = spot_id
        self._is_free = True

    def is_spot_free(self):
        return self._is_free

    def occupy_spot(self):
        self._is_free = False

    def release_spot(self):
        self._is_free = True

    def get_spot_id(self):
        return self._spot_id
