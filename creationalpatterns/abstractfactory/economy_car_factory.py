from .car_factory import CarFactory
from .economy_car_interior import EconomyCarInterior
from .economy_car_exterior import EconomyCarExterior


# Step 5: Concrete Factories
class EconomyCarFactory(CarFactory):
    def __init__(self, brand):
        self.brand = brand

    def create_interior(self):
        return EconomyCarInterior()

    def create_exterior(self):
        return EconomyCarExterior()
