from abc import ABC, abstractmethod


# Aggregate interface
class BookCollection(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

    @abstractmethod
    def create_reverse_iterator(self):
        pass
