class Seat:
    def __init__(self, seat_id, category):
        self._seat_id = seat_id
        self._category = category

    def get_seat_id(self):
        return self._seat_id
