from abc import ABC
import threading


class ParkingSpotManager(ABC):
    def __init__(self, spots, strategy):
        self.spots = spots
        self.strategy = strategy
        self._lock = threading.Lock()

    def park(self):
        with self._lock:
            spot = self.strategy.select_spot(self.spots)
            if spot is None:
                return None
            spot.occupy_spot()
            return spot

    def un_park(self, spot):
        with self._lock:
            spot.release_spot()

    def has_free_spot(self):
        with self._lock:
            return any(spot.is_spot_free() for spot in self.spots)
