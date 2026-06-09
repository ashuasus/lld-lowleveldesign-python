from abc import ABC, abstractmethod


# GOOD: This follows ISP - Multiple focused interfaces following ISP
class MaintenanceTasks(ABC):
    @abstractmethod
    def clean_the_kitchen(self):
        pass

    @abstractmethod
    def re_stock_groceries(self):
        pass
