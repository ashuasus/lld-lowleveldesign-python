class Screen:
    def __init__(self, screen_id, seats):
        self._screen_id = screen_id
        self._seats = seats
        self._shows_by_date = {}

    def get_seats(self):
        return self._seats

    def add_show(self, show):
        date = show.get_show_date()
        if date not in self._shows_by_date:
            self._shows_by_date[date] = []
        self._shows_by_date[date].append(show)

    def get_shows(self, date):
        return self._shows_by_date.get(date, [])
