from abc import ABC, abstractmethod


# Step 1: Abstract Product interfaces - Define product families
class CarInterior(ABC):
    @abstractmethod
    def add_interior_components(self):
        pass
