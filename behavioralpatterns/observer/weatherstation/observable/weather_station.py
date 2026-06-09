from .weather_observable import WeatherObservable


# Concrete Observable (Subject)
class WeatherStation(WeatherObservable):
    def __init__(self):
        self._observers = []
        self._temperature = 0
        self._humidity = 0
        self._pressure = 0

    def add_observer(self, observer):
        self._observers.append(observer)
        print("[+] Observer registered: " + observer.__class__.__name__)

    def remove_observer(self, observer):
        self._observers.remove(observer)
        print("[-] Observer removed: " + observer.__class__.__name__)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def set_weather_readings(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

    def get_temperature(self):
        return self._temperature

    def get_humidity(self):
        return self._humidity

    def get_pressure(self):
        return self._pressure

    def __str__(self):
        return "WeatherStation{temperature=" + str(self._temperature) + ", humidity=" + str(self._humidity) + ", pressure=" + str(self._pressure) + "}"
