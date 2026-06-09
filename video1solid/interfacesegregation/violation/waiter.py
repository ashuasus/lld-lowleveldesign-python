from .restaurant_employee import RestaurantEmployee


# BAD: This class violates ISP(clients shouldn't depend on unused interfaces)
# Bloated class with empty or error-throwing methods
# This Waiter is forced to implement methods it doesn't need
class Waiter(RestaurantEmployee):
    def take_order(self):
        print("Taking order...")

    def serve_food_and_drinks(self):
        print("Serving food and drinks...")

    def clean_the_kitchen(self):
        # Forced to implement but doesn't make sense for a waiter
        raise AssertionError("Detail Message: Waiter cannot clean the kitchen!")

    def prepare_food(self):
        # Forced to implement but doesn't make sense for a waiter
        raise AssertionError("Detail Message: Waiter cannot prepare food!")

    def decide_menu(self):
        # Forced to implement but doesn't make sense for a waiter
        raise AssertionError("Detail Message: Waiter cannot decide the menu!")
