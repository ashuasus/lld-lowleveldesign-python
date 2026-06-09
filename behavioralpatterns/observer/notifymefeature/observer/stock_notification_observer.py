from abc import ABC, abstractmethod


# Observer interface for stock availability notifications
class StockNotificationObserver(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_notification_method(self):
        pass

    @abstractmethod
    def get_user_id(self):
        pass
