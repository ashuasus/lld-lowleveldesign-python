from abc import ABC, abstractmethod


# Approach without bridge: breathing logic hardcoded inside LivingThings
class LivingThings(ABC):
    @abstractmethod
    def breathe(self):
        pass
