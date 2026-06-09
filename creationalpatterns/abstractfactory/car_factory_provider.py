from enum import Enum
from .economy_car_factory import EconomyCarFactory
from .luxury_car_factory import LuxuryCarFactory


class CarType(Enum):
    ECONOMY = "ECONOMY"
    LUXURY = "LUXURY"
    PREMIUM = "PREMIUM"


# Step 6: Factory Provider
class CarFactoryProvider:
    def get_factory(self, car_type, brand):
        if car_type == CarType.ECONOMY:
            return EconomyCarFactory(brand)
        elif car_type in (CarType.PREMIUM, CarType.LUXURY):
            return LuxuryCarFactory(brand)
        else:
            raise ValueError("Unknown car type: " + str(car_type))
