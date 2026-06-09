from abc import ABC, abstractmethod


# GOOD: This follows ISP - Multiple focused interfaces following ISP
class ChefTasks(ABC):
    @abstractmethod
    def prepare_food(self):
        pass

    @abstractmethod
    def decide_menu(self):
        pass
