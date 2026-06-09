from ..entities.booking import Booking
from ..entities.payment import Payment
from ..enums.payment_status import PaymentStatus


class BookingService:
    def __init__(self):
        self._bookings = {}

    def book(self, user, show, seats):
        if not show.lock_seats(seats):
            raise RuntimeError("Seat unavailable")

        # simulated payment flow
        payment = Payment(PaymentStatus.SUCCESS)

        if payment.get_status() == PaymentStatus.SUCCESS:
            show.confirm_seats(seats)
            booking = Booking(user, show, seats, payment)
            self._bookings[booking.get_booking_id()] = booking
            return booking
        else:
            show.release_seats(seats)
            raise RuntimeError("Payment failed")

    def get_booking(self, booking_id):
        return self._bookings.get(booking_id)

    def get_bookings_for_user(self, user):
        return [b for b in self._bookings.values() if b.get_user() == user]
