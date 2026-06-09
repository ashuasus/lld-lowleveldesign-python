from abc import ABC, abstractmethod


# Step 1: Define the Component Interface
class BasePizza(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass
