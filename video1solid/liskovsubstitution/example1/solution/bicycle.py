from .bike import Bike


# GOOD: Following LSP
# Subclass of Bike - implements all Bike class behavior
# As Bicycles do not have engines, we need not implement Engine interface
class Bicycle(Bike):
    def __init__(self, brand, has_gears, speed):
        self.brand = brand
        self.has_gears = has_gears
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 10
        print("Bicycle Speed: " + str(self.speed))

    def apply_brakes(self):
        self.speed = self.speed - 5
        print("Bicycle Speed: " + str(self.speed))
