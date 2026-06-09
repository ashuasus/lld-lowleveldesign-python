from .chef import Chef
from .waiter import Waiter


# Usage example - Following ISP
def main():
    # Create the objects
    # Now classes only implement what they actually support
    chef = Chef()
    waiter = Waiter()

    # Use the objects
    # These work perfectly - no forced implementations
    chef.prepare_food()
    chef.decide_menu()
    # These work perfectly - no forced implementations
    waiter.take_order()
    waiter.serve_food_and_drinks()


if __name__ == "__main__":
    main()
