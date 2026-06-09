from ..service.theatre_service import TheatreService


class TheatreController:
    def __init__(self):
        self._theatre_service = TheatreService()

    def add_theatre(self, theatre):
        self._theatre_service.add_theatre(theatre)

    def get_movies(self, city, date):
        return self._theatre_service.get_movies(city, date)

    def get_theatres(self, city, movie, date):
        return self._theatre_service.get_theatres(city, movie, date)

    def get_shows(self, movie, date, theatre):
        return self._theatre_service.get_shows(movie, date, theatre)
