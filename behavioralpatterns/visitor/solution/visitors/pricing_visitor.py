from .i_room_visitor import IRoomVisitor


# Pricing visitor - demonstrates adding new operations easily
class PricingVisitor(IRoomVisitor):
    def __init__(self):
        self._total_revenue = 0

    def visit_standard_room(self, room):
        price = 1000.0
        self._total_revenue += price
        print("Pricing: Standard room " + room.get_room_number() +
              " - Rs." + str(price) + "/night")

    def visit_deluxe_room(self, room):
        price = 2000.0
        self._total_revenue += price
        print("Pricing: Deluxe room " + room.get_room_number() +
              " - Rs." + str(price) + "/night")

    def visit_suite_room(self, room):
        price = 5000.0
        self._total_revenue += price
        print("Pricing: Suite " + room.get_room_number() +
              " - Rs." + str(price) + "/night")

    def get_total_revenue(self):
        return self._total_revenue
