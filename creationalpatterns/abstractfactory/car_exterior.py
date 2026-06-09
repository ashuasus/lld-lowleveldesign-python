from abc import ABC, abstractmethod


# Step 1: Abstract Product interfaces - Define product families
class CarExterior(ABC):
    @abstractmethod
    def add_exterior_components(self):
        pass
