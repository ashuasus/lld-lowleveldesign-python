from abc import ABC, abstractmethod


# Target or Adapter Interface
class WeighingMachineAdapter(ABC):
    @abstractmethod
    def get_weight_in_kg(self):
        pass
