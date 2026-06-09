from .weather_observer import WeatherObserver


# Concrete Observer 4 - Forecast Display - Predicts weather based on pressure changes
class ForecastDisplay(WeatherObserver):
    def __init__(self, weather_station):
        self._weather_station = weather_station
        weather_station.add_observer(self)

    def update(self):
        print("Updating weather data to do some analytics: " + str(self._weather_station))
        self.display()

    def display(self):
        print("Forecast Details: Displaying information about Rain, " +
              "Temperature Trends, Significant Weather Events and other phenomemnon...")
