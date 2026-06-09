from abc import ABC, abstractmethod


# GOOD: Following OCP using interfaces and polymorphism
class InvoiceDao(ABC):
    @abstractmethod
    def save(self):
        pass
