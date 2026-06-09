class ReservationRepository:
    def __init__(self):
        self._reservations = {}

    def save(self, reservation):
        self._reservations[reservation.get_reservation_id()] = reservation

    def find_by_id(self, reservation_id):
        return self._reservations.get(reservation_id)

    def remove(self, reservation_id):
        self._reservations.pop(reservation_id, None)

    def get_all(self):
        return self._reservations
