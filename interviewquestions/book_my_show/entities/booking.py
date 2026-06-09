import uuid


class Booking:
    def __init__(self, user, show, seats, payment):
        self._booking_id = uuid.uuid4()
        self._user = user
        self._show = show
        self._seats = seats
        self._payment = payment

    def get_booking_id(self):
        return self._booking_id

    def get_user(self):
        return self._user

    def get_payment(self):
        return self._payment
