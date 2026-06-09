import threading
from .vehicle_status import VehicleStatus
from .date_interval import DateInterval


class VehicleInventoryManager:
    def __init__(self):
        self._vehicles = {}
        self._vehicle_booking_ids = {}
        self._vehicle_locks = {}
        self._reservation_repository = None

    def add_vehicle(self, vehicle):
        self._vehicles[vehicle.get_vehicle_id()] = vehicle

    def get_vehicle(self, vehicle_id):
        return self._vehicles.get(vehicle_id)

    def set_reservation_repository(self, reservation_repository):
        self._reservation_repository = reservation_repository

    def _lock_for_vehicle(self, vehicle_id):
        self._vehicle_locks.setdefault(vehicle_id, threading.Lock())
        return self._vehicle_locks[vehicle_id]

    def is_available(self, vehicle_id, from_date, to_date):
        vehicle = self._vehicles.get(vehicle_id)
        if vehicle is None:
            return False
        if vehicle.get_vehicle_status() == VehicleStatus.MAINTENANCE:
            return False

        requested = DateInterval(from_date, to_date)
        reservation_ids = self._vehicle_booking_ids.get(vehicle_id)
        if not reservation_ids:
            return True

        for reservation_id in reservation_ids:
            reservation = self._reservation_repository.find_by_id(reservation_id)
            if reservation is None:
                continue
            booked_from = reservation.get_date_booked_from()
            booked_till = reservation.get_date_booked_to()
            booked_interval = DateInterval(booked_from, booked_till)
            if booked_interval.overlaps(requested):
                return False
        return True

    def reserve(self, vehicle_id, reservation_id, from_date, to_date):
        lock = self._lock_for_vehicle(vehicle_id)
        with lock:
            if not self.is_available(vehicle_id, from_date, to_date):
                return False
            if vehicle_id not in self._vehicle_booking_ids:
                self._vehicle_booking_ids[vehicle_id] = []
            self._vehicle_booking_ids[vehicle_id].append(reservation_id)
            self._vehicles[vehicle_id].set_status(VehicleStatus.BOOKED)
            return True

    def release(self, vehicle_id, reservation_id):
        lock = self._lock_for_vehicle(vehicle_id)
        with lock:
            ids = self._vehicle_booking_ids.get(vehicle_id)
            if ids is not None:
                ids.remove(reservation_id)
            still_booked = self._vehicle_booking_ids.get(vehicle_id)
            if not still_booked:
                self._vehicles[vehicle_id].set_status(VehicleStatus.AVAILABLE)

    def get_available_vehicles(self, vehicle_type, from_date, to_date):
        return [v for v in self._vehicles.values()
                if v.get_vehicle_type() == vehicle_type
                and self.is_available(v.get_vehicle_id(), from_date, to_date)]
