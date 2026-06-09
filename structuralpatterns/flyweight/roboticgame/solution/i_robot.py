from abc import ABC, abstractmethod


# Flyweight (Interface) - for the flyweight object – defines methods that use extrinsic state.
class IRobot(ABC):
    # CoordinateX and CoordinateY are extrinsic data - unique to each object
    @abstractmethod
    def display(self, x, y):
        pass
