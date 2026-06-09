from abc import ABC, abstractmethod


# BAD: This class violates ISP
# This is a fat interface
# One large interface forcing all implementers to define unused methods
class RestaurantEmployee(ABC):
    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def decide_menu(self):
        pass

    @abstractmethod
    def serve_food_and_drinks(self):
        pass

    @abstractmethod
    def take_order(self):
        pass

    @abstractmethod
    def clean_the_kitchen(self):
        pass
