from .observable.weather_station import WeatherStation
from .observer.current_conditions_display import CurrentConditionsDisplay
from .observer.forecast_display import ForecastDisplay


# Client code to demonstrate the Observer Pattern
def main():
    print("###### State Design Pattern ######")
    # Create the weather station (observable/subject)
    weather_station = WeatherStation()

    # Create displays (observers)
    current_display = CurrentConditionsDisplay(weather_station)
    forecast_display = ForecastDisplay(weather_station)

    print("===>>> Initial Weather Update")
    weather_station.set_weather_readings(80, 65, 30.4)

    print("===>>> Second Weather Update")
    weather_station.set_weather_readings(82, 70, 29.2)

    # Remove forecast display
    weather_station.remove_observer(forecast_display)

    print("===>>> Third Weather Update")
    weather_station.set_weather_readings(70, 21, 29.2)
    # Forecast display will not be notified


if __name__ == "__main__":
    main()
