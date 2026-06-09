from abc import ABC, abstractmethod


class Keyboard(ABC):
    @abstractmethod
    def get_specifications(self):
        pass
