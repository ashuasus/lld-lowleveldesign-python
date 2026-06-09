from .order_facade import OrderFacade


# Client Usage
def main():
    print("====== Facade Design Pattern Demo ======")
    # Client interacts with a simple Facade, not with all subsystems.
    order_facade = OrderFacade()

    # Place order with one call to Facade
    order_facade.place_order("MacBook Pro", "Credit Card")

    # Place another order with one call to Facade
    order_facade.place_order("Cricket Bat", "UPI")


if __name__ == "__main__":
    main()
