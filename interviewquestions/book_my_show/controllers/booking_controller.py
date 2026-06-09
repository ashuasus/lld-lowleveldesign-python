from ..service.booking_service import BookingService


class BookingController:
    def __init__(self):
        self._booking_service = BookingService()

    def create_booking(self, user, show, seats):
        booking = self._booking_service.book(user, show, seats)
        return booking

    def get_booking(self, booking_id):
        return self._booking_service.get_booking(booking_id)

    def get_bookings_for_user(self, user):
        return self._booking_service.get_bookings_for_user(user)
