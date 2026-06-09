from abc import ABC, abstractmethod


class ParkingSpotLookupStrategy(ABC):
    @abstractmethod
    def select_spot(self, spots):
        pass
