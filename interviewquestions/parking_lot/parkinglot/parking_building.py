from ..ticket import Ticket


class ParkingBuilding:
    def __init__(self, levels, cost_computation):
        self._levels = levels

    def allocate(self, vehicle):
        for level in self._levels:
            if level.has_availability(vehicle.get_vehicle_type()):
                spot = level.park(vehicle.get_vehicle_type())
                if spot is not None:
                    ticket = Ticket(vehicle, level, spot)
                    print("Parking allocated at level: " + str(level.get_level_number()) + " spot: " + spot.get_spot_id())
                    return ticket
        raise RuntimeError("Parking Full")

    def release(self, ticket):
        ticket.get_level().un_park(
            ticket.get_vehicle().get_vehicle_type(),
            ticket.get_spot()
        )
