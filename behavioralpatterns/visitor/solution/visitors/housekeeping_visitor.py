from .i_room_visitor import IRoomVisitor


# Concrete Visitor - demonstrates adding new operations easily
class HousekeepingVisitor(IRoomVisitor):
    def visit_standard_room(self, room):
        print("Housekeeping: Cleaning standard room " +
              room.get_room_number() + " (30 minutes)")

    def visit_deluxe_room(self, room):
        print("Housekeeping: Cleaning deluxe room " +
              room.get_room_number() +
              (" including jacuzzi" if room.has_jacuzzi() else "") +
              " (45 minutes)")

    def visit_suite_room(self, room):
        print("Housekeeping: Cleaning suite " +
              room.get_room_number() + " with " +
              str(room.get_number_of_rooms()) + " rooms (90 minutes)")
