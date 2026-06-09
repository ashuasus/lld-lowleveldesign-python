from .waiter import Waiter


# Usage example - showing the problem
def main():
    waiter = Waiter()
    # Works fine
    waiter.take_order()
    waiter.serve_food_and_drinks()

    # These will throw exceptions
    waiter.prepare_food()  # forced implementation
    waiter.decide_menu()  # forced implementation
    waiter.clean_the_kitchen()  # forced implementation


if __name__ == "__main__":
    main()
