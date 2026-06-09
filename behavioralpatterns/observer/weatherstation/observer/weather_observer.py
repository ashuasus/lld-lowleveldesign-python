from abc import ABC, abstractmethod


# Observer interface - defines the update method
class WeatherObserver(ABC):
    @abstractmethod
    def update(self):
        pass
