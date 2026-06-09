from .weather_observer import WeatherObserver


# Concrete Observer 1 - Current Conditions Display (on TV or Mobile)
class CurrentConditionsDisplay(WeatherObserver):
    def __init__(self, weather_station):
        self._weather_station = weather_station
        weather_station.add_observer(self)

    def update(self):
        print("Saving weather data... ")
        self.display()

    def display(self):
        print("Current Weather Conditions: " + str(self._weather_station))
