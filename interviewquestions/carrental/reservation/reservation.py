from .reservation_status import ReservationStatus


class Reservation:
    def __init__(self, reservation_id, vehicle_id, user_id, date_booked_from, date_booked_to, reservation_type):
        self._reservation_id = reservation_id
        self._vehicle_id = vehicle_id
        self._user_id = user_id
        self._date_booked_from = date_booked_from
        self._date_booked_to = date_booked_to
        self._reservation_type = reservation_type
        self._reservation_status = ReservationStatus.SCHEDULED

    def get_reservation_id(self):
        return self._reservation_id

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_user_id(self):
        return self._user_id

    def get_date_booked_from(self):
        return self._date_booked_from

    def get_date_booked_to(self):
        return self._date_booked_to

    def get_reservation_type(self):
        return self._reservation_type

    def get_reservation_status(self):
        return self._reservation_status

    def set_reservation_status(self, reservation_status):
        self._reservation_status = reservation_status
