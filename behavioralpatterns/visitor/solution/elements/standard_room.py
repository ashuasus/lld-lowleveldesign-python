from .i_room import IRoom


# Concrete Element - Different room types
class StandardRoom(IRoom):
    def __init__(self, room_number):
        self._room_number = room_number

    def accept(self, visitor):
        visitor.visit_standard_room(self)

    def get_room_number(self):
        return self._room_number
