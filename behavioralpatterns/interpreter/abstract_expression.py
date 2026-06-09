from abc import ABC, abstractmethod


# Abstract Expression interface
class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass
