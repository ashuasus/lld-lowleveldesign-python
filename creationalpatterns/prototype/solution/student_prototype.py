from abc import ABC, abstractmethod


# Prototype interface
class StudentPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass
