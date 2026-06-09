from .bike import Bike
from .engine import Engine


# Subclass of Bike - implements all Bike class behavior
class MotorCycle(Bike, Engine):
    def __init__(self, company, speed):
        self.company = company
        self.is_engine_on = False
        self.speed = speed

    def turn_on_engine(self):
        self.is_engine_on = True
        print("Engine is ON!")

    def turn_off_engine(self):
        self.is_engine_on = False
        print("Engine is OFF!")

    def accelerate(self):
        self.speed = self.speed + 10
        print("MotorCycle Speed: " + str(self.speed))

    def apply_brakes(self):
        self.speed = self.speed - 5
        print("MotorCycle Speed: " + str(self.speed))
