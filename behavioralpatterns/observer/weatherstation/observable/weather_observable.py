from abc import ABC, abstractmethod


# Observable(Subject) interface
class WeatherObservable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def set_weather_readings(self, temperature, humidity, pressure):
        pass
