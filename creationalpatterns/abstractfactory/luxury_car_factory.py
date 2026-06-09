from .car_factory import CarFactory
from .luxury_car_interior import LuxuryCarInterior
from .luxury_car_exterior import LuxuryCarExterior


# Step 5: Concrete Factories
class LuxuryCarFactory(CarFactory):
    def __init__(self, brand):
        self.brand = brand

    def create_interior(self):
        return LuxuryCarInterior()

    def create_exterior(self):
        return LuxuryCarExterior()
