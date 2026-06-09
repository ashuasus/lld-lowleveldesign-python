class ParkingLot:
    def __init__(self, building, entrance_gate, exit_gate):
        self._building = building
        self._entrance_gate = entrance_gate
        self._exit_gate = exit_gate

    def vehicle_arrives(self, vehicle):
        return self._entrance_gate.enter(self._building, vehicle)

    def vehicle_exits(self, ticket, payment):
        self._exit_gate.complete_exit(self._building, ticket, payment)
