from .bike import Bike


# This class violates LSP!
class Bicycle(Bike):
    def __init__(self, brand, has_gears, speed):
        self.brand = brand
        self.has_gears = has_gears
        self.speed = speed

    # LSP Violation: Strengthening preconditions
    # Bicycle changes the behavior of turn_on_engine
    def turn_on_engine(self):
        raise AssertionError("Detail Message: Bicycle has no engine!")

    # Bicycle changes the behavior of turn_off_engine
    def turn_off_engine(self):
        raise AssertionError("Detail Message: Bicycle has no engine!")

    def accelerate(self):
        self.speed = self.speed + 10
        print("Bicycle Speed: " + str(self.speed))

    def apply_brakes(self):
        self.speed = self.speed - 5
        print("Bicycle Speed: " + str(self.speed))
