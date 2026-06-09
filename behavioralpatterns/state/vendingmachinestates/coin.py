from enum import Enum


class Coin(Enum):
    PENNY = 1
    NICKEL = 5
    DIME = 10
    QUARTER = 25

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value
