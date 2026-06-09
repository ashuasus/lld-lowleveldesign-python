from abc import ABC, abstractmethod


class Mouse(ABC):
    @abstractmethod
    def get_specifications(self):
        pass
