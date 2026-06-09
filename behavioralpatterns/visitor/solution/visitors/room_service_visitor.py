from .i_room_visitor import IRoomVisitor


# Pricing visitor - demonstrates adding new operations easily
class RoomServiceVisitor(IRoomVisitor):
    def __init__(self, order_details):
        self._order_details = order_details

    def visit_standard_room(self, room):
        print("Room Service: Delivering " + self._order_details +
              " to standard room " + room.get_room_number())

    def visit_deluxe_room(self, room):
        print("Room Service: Premium delivery of " + self._order_details +
              " to deluxe room " + room.get_room_number() +
              " with complimentary champagne")

    def visit_suite_room(self, room):
        print("Room Service: VIP delivery of " + self._order_details +
              " to suite " + room.get_room_number() +
              " with full dining setup")
