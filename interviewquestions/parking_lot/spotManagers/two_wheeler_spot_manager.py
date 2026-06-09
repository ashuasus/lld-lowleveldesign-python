from .parking_spot_manager import ParkingSpotManager


class TwoWheelerSpotManager(ParkingSpotManager):
    def __init__(self, spots, strategy):
        super().__init__(spots, strategy)
