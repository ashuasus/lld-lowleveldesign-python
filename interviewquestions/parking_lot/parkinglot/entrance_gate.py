class EntranceGate:
    def enter(self, building, vehicle):
        return building.allocate(vehicle)
