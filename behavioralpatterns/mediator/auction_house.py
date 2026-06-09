from .auction_mediator import AuctionMediator


# Concrete Mediator
class AuctionHouse(AuctionMediator):
    def __init__(self, item_name, starting_price):
        self.item_name = item_name
        self.current_highest_bid = starting_price
        self.current_highest_bidder = None
        self.bidders = []
        print("[+] Auction House created for item: " + item_name + " with initial bid of $" + str(starting_price))

    def register_bidder(self, bidder):
        self.bidders.append(bidder)
        print("[+] " + bidder.get_name() + " has joined the auction for " + self.item_name)

    def place_bid(self, bidder, bid_amount):
        # Check if the bid is valid
        if bid_amount <= self.current_highest_bid:
            print(bidder.get_name() + " bid of $" + str(bid_amount) + " is too low. Current highest bid is $" + str(self.current_highest_bid))
            return

        # Update the highest bid
        self.current_highest_bid = bid_amount
        self.current_highest_bidder = bidder
        print("\n===> [New Bid Accepted]" + " Info: {Bidder: " + bidder.get_name() + ", Bid Amount: " + str(bid_amount) + "}")
        for colleague in self.bidders:
            if colleague.get_name() != bidder.get_name():
                # Notify other bidders about the new bid
                colleague.receive_bid_notification(bid_amount)

    def close_auction(self):
        if self.current_highest_bidder is not None:
            print("\n===> [AUCTION UPDATE]")
            print("[+] Auction closed! Winner is " + self.current_highest_bidder.get_name() +
                  " with a bid of $" + str(self.current_highest_bid) + " for " + self.item_name)
        else:
            print("Auction closed with no bids.")
