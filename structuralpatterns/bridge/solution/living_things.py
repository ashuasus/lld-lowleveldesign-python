from abc import ABC, abstractmethod


# Step 3: Abstraction for LivingThings
class LivingThings(ABC):
    def __init__(self, breathing_process):
        # Reference to Implementor
        self.breathing_process = breathing_process

    # Operation implemented by Implementor
    @abstractmethod
    def breathe(self):
        pass
