from abc import ABC, abstractmethod


# Observable interface
class StockAvailabilityObservable(ABC):
    @abstractmethod
    def add_stock_observer(self, observer):
        pass

    @abstractmethod
    def remove_stock_observer(self, observer):
        pass

    @abstractmethod
    def notify_stock_observers(self):
        pass

    @abstractmethod
    def purchase(self, quantity):
        pass

    @abstractmethod
    def restock(self, quantity):
        pass
