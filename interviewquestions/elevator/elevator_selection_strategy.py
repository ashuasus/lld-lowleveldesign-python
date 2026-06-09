from abc import ABC, abstractmethod

class ElevatorSelectionStrategy(ABC):
    @abstractmethod
    def select_elevator(self, controllers, request_floor, direction):
        pass
