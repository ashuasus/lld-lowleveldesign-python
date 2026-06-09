from abc import ABC, abstractmethod


# Step 1: Implementor (Breathing process)
class BreathingProcess(ABC):
    @abstractmethod
    def breathe(self):
        pass
