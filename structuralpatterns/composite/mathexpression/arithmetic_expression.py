from abc import ABC, abstractmethod


# Component Interface
class ArithmeticExpression(ABC):
    @abstractmethod
    def evaluate(self):
        pass
