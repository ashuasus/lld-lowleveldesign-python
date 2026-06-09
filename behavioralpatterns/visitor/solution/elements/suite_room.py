from .i_room import IRoom


# Concrete Element - Different room types
class SuiteRoom(IRoom):
    def __init__(self, room_number, number_of_rooms):
        self._room_number = room_number
        self._number_of_rooms = number_of_rooms

    def accept(self, visitor):
        visitor.visit_suite_room(self)

    def get_room_number(self):
        return self._room_number

    def get_number_of_rooms(self):
        return self._number_of_rooms
