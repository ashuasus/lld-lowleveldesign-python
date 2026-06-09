from .vehicle import Vehicle


# Concrete context subclass
class HybridVehicle(Vehicle):
    def __init__(self, drive_strategy):
        super().__init__(drive_strategy)
