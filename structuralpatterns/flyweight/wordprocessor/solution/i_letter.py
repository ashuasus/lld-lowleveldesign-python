from abc import ABC, abstractmethod


# Flyweight (Interface) - for the flyweight object – defines methods that use extrinsic state.
class ILetter(ABC):
    # The position(row,column) is extrinsic data - unique to each object
    @abstractmethod
    def display(self, row, column):
        pass
