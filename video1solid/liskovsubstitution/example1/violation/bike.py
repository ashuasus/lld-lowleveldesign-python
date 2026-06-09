from abc import ABC, abstractmethod


# BAD: This design violates LSP
class Bike(ABC):
    @abstractmethod
    def turn_on_engine(self):
        pass

    @abstractmethod
    def turn_off_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def apply_brakes(self):
        pass
