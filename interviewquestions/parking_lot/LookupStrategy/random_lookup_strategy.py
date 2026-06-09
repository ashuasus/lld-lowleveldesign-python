from .parking_spot_lookup_strategy import ParkingSpotLookupStrategy


class RandomLookupStrategy(ParkingSpotLookupStrategy):
    def select_spot(self, spots):
        for spot in spots:
            if spot.is_spot_free():
                return spot
        return None
