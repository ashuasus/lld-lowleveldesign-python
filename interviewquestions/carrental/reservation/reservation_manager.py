import itertools
from .reservation import Reservation
from .reservation_repository import ReservationRepository
from .reservation_status import ReservationStatus


class ReservationManager:
    _id_counter = itertools.count(20000)

    def __init__(self, inventory):
        self._inventory = inventory
        self._reservation_repository = ReservationRepository()
        self._inventory.set_reservation_repository(self._reservation_repository)

    def find_by_id(self, reservation_id):
        return self._reservation_repository.find_by_id(reservation_id)

    def create_reservation(self, vehicle_id, user, from_date, to_date, reservation_type):
        reservation_id = next(ReservationManager._id_counter)
        reserved = self._inventory.reserve(vehicle_id, reservation_id, from_date, to_date)

        if not reserved:
            raise RuntimeError("Vehicle not available for selected dates")

        reservation = Reservation(reservation_id, vehicle_id, user.get_user_id(), from_date, to_date, reservation_type)
        self._reservation_repository.save(reservation)
        return reservation

    def cancel_reservation(self, reservation_id):
        r = self._reservation_repository.find_by_id(reservation_id)
        if r is None:
            raise RuntimeError("Reservation not found")
        r.set_reservation_status(ReservationStatus.CANCELLED)
        self._inventory.release(r.get_vehicle_id(), r.get_reservation_id())
        self._reservation_repository.remove(reservation_id)

    def start_trip(self, reservation_id):
        r = self._reservation_repository.find_by_id(reservation_id)
        if r is None:
            raise RuntimeError("Reservation not found")
        r.set_reservation_status(ReservationStatus.IN_USE)

    def submit_vehicle(self, reservation_id):
        r = self._reservation_repository.find_by_id(reservation_id)
        if r is None:
            raise RuntimeError("Reservation not found")
        r.set_reservation_status(ReservationStatus.COMPLETED)
        self._inventory.release(r.get_vehicle_id(), r.get_reservation_id())

    def remove(self, reservation_id):
        self._reservation_repository.remove(reservation_id)
