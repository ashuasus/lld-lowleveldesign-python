import threading
from ..enums.seat_status import SeatStatus


class Show:
    def __init__(self, movie, screen, show_date, start_time):
        self._movie = movie
        self._show_date = show_date
        self._start_time = start_time
        self._seat_status_map = {}
        self._seat_locks = {}

        for seat in screen.get_seats():
            self._seat_status_map[seat.get_seat_id()] = SeatStatus.AVAILABLE
            self._seat_locks[seat.get_seat_id()] = threading.Lock()

    def get_movie(self):
        return self._movie

    def get_show_date(self):
        return self._show_date

    def get_start_time(self):
        return self._start_time

    def lock_seats(self, seat_ids):
        sorted_ids = sorted(seat_ids)
        acquired_locks = []

        try:
            # Phase 1: acquire all locks
            for seat_id in sorted_ids:
                lock = self._seat_locks[seat_id]
                lock.acquire()
                acquired_locks.append(lock)

            # Phase 2: validate availability
            for seat_id in sorted_ids:
                if self._seat_status_map[seat_id] != SeatStatus.AVAILABLE:
                    return False

            # Phase 3: mark LOCKED
            for seat_id in sorted_ids:
                self._seat_status_map[seat_id] = SeatStatus.LOCKED

            return True

        finally:
            # Phase 4: release locks
            for lock in acquired_locks:
                lock.release()

    def confirm_seats(self, seat_ids):
        for seat_id in seat_ids:
            self._seat_status_map[seat_id] = SeatStatus.BOOKED

    def release_seats(self, seat_ids):
        for seat_id in seat_ids:
            self._seat_status_map[seat_id] = SeatStatus.AVAILABLE
