from abc import ABC, abstractmethod


# Step 3: Abstract Creator class
class ShapeFactory(ABC):
    # Factory method - to be implemented by subclasses
    @abstractmethod
    def create_shape(self):
        pass
