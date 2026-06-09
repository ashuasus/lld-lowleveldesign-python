from abc import ABC, abstractmethod


# Colleague Interface(aka Component Interface)
class IColleague(ABC):
    @abstractmethod
    def place_bid(self, amount):
        pass

    @abstractmethod
    def receive_bid_notification(self, bid_amount):
        pass

    @abstractmethod
    def get_name(self):
        pass
