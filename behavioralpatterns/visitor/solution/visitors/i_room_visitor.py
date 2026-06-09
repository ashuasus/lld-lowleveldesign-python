from abc import ABC, abstractmethod


# Visitor interface - defines operations
class IRoomVisitor(ABC):
    @abstractmethod
    def visit_standard_room(self, room):
        pass

    @abstractmethod
    def visit_deluxe_room(self, room):
        pass

    @abstractmethod
    def visit_suite_room(self, room):
        pass
