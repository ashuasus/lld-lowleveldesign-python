from abc import ABC, abstractmethod


# Element interface - represents rooms(elements) that can be visited
class IRoom(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
