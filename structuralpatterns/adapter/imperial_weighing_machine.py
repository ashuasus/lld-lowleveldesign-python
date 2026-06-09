from abc import ABC, abstractmethod


# Adaptee Interface
# Third-party weighing machine (US model) – returns pounds
class ImperialWeighingMachine(ABC):
    @abstractmethod
    def get_weight_in_pounds(self):
        pass
