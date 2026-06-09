class TheatreService:
    def __init__(self):
        self._city_theatres = {}

    def add_theatre(self, theatre):
        city = theatre.get_city()
        if city not in self._city_theatres:
            self._city_theatres[city] = []
        self._city_theatres[city].append(theatre)

    def get_movies(self, city, date):
        movies = set()
        theatres = self._city_theatres.get(city, [])

        for theatre in theatres:
            for screen in theatre.get_screens():
                for show in screen.get_shows(date):
                    movies.add(show.get_movie())
        return movies

    def get_theatres(self, city, movie, date):
        theatres = self._city_theatres.get(city, [])
        return [t for t in theatres if any(
            any(show.get_movie() == movie for show in screen.get_shows(date))
            for screen in t.get_screens()
        )]

    def get_shows(self, movie, date, theatre):
        result = []
        for screen in theatre.get_screens():
            for show in screen.get_shows(date):
                if show.get_movie() == movie:
                    result.append(show)
        return result
