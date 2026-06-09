from abc import ABC, abstractmethod


# Step 1: Define the Product interface
class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass

    @abstractmethod
    def draw(self):
        pass
