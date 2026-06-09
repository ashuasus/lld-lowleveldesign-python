from .i_colleague import IColleague


# Concrete Colleague/Component
class Bidder(IColleague):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        mediator.register_bidder(self)

    def place_bid(self, amount):
        print("\n===> [Placing Bid] " + self.name + " is attempting to bid $" + str(amount))
        self.mediator.place_bid(self, amount)

    def receive_bid_notification(self, bid_amount):
        print("[+] Bidder " + self.name + " has received a new bid notification of: " + str(bid_amount))

    def get_name(self):
        return self.name
