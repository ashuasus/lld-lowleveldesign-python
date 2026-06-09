from abc import ABC, abstractmethod


# GOOD: This follows ISP - Multiple focused interfaces following ISP
class WaiterTasks(ABC):
    @abstractmethod
    def serve_food_and_drinks(self):
        pass

    @abstractmethod
    def take_order(self):
        pass
