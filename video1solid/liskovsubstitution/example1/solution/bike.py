from abc import ABC, abstractmethod


class Bike(ABC):
    # All Bikes can do these things
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def apply_brakes(self):
        pass
