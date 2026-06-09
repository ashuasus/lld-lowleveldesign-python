from abc import ABC, abstractmethod


# Mediator Interface
class AuctionMediator(ABC):
    @abstractmethod
    def register_bidder(self, bidder):
        pass

    @abstractmethod
    def place_bid(self, bidder, bid_amount):
        pass

    @abstractmethod
    def close_auction(self):
        pass
