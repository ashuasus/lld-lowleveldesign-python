from .vehicle import Vehicle


# Concrete context subclass
class GoodsVehicle(Vehicle):
    def __init__(self, drive_strategy):
        super().__init__(drive_strategy)
