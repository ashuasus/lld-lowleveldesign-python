from .i_room import IRoom


# Concrete Element - Different room types
class DeluxeRoom(IRoom):
    def __init__(self, room_number, has_jacuzzi):
        self._room_number = room_number
        self._has_jacuzzi = has_jacuzzi

    def accept(self, visitor):
        visitor.visit_deluxe_room(self)

    def get_room_number(self):
        return self._room_number

    def has_jacuzzi(self):
        return self._has_jacuzzi
