from abc import ABC, abstractmethod


# Strategy interface - defines the contract for drive behavior
class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass
