from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def turn_on_engine(self):
        pass

    @abstractmethod
    def turn_off_engine(self):
        pass
