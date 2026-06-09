from .auction_house import AuctionHouse
from .bidder import Bidder


# Client
def main():
    print("\n###### Mediator Design Pattern ######")
    print("\n===> Welcome to the Auction House!\n")

    # Create a Mediator
    auction_house = AuctionHouse("Vintage Guitar", 100.0)

    # Create Colleagues/Components
    alice = Bidder("Alice", auction_house)
    bob = Bidder("Bob", auction_house)
    charlie = Bidder("Charlie", auction_house)

    # Use Colleagues/Components
    alice.place_bid(150.0)
    bob.place_bid(250.0)
    charlie.place_bid(300.0)
    alice.place_bid(300.0)  # Will not be accepted
    bob.place_bid(900.0)  # Winner

    # Admin closes the auction
    auction_house.close_auction()


if __name__ == "__main__":
    main()
