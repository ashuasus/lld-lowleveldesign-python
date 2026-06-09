from datetime import date, time
from .controllers.theatre_controller import TheatreController
from .controllers.booking_controller import BookingController
from .entities.movie import Movie
from .entities.screen import Screen
from .entities.theatre import Theatre
from .entities.seat import Seat
from .entities.show import Show
from .entities.user import User
from .enums.city import City
from .enums.seat_category import SeatCategory


class BookMyShowApp:
    def __init__(self):
        self._theatre_controller = None
        self._booking_controller = None

    @staticmethod
    def main():
        app = BookMyShowApp()
        app.initialize()
        app.user_flow()

    def initialize(self):
        self._theatre_controller = TheatreController()
        self._booking_controller = BookingController()

        # 1. Create Movies
        baahubali = Movie("BAAHUBALI")
        avengers = Movie("AVENGERS")

        # 2. Create Theatre -> Screen -> Seats
        inox_screen1 = Screen(1, self._create_seats())
        inox_theatre_bangalore = Theatre("INOX", City.BANGALORE, [inox_screen1])

        pvr_screen1 = Screen(1, self._create_seats())
        pvr_theatre_delhi = Theatre("PVR", City.DELHI, [pvr_screen1])

        self._theatre_controller.add_theatre(inox_theatre_bangalore)
        self._theatre_controller.add_theatre(pvr_theatre_delhi)

        # 3. Create Shows
        today = date.today()
        inox_morning_show_today = Show(baahubali, inox_screen1, today, time(8, 0))
        inox_afternoon_show_today = Show(baahubali, inox_screen1, today, time(15, 0))
        inox_evening_show_today = Show(avengers, inox_screen1, today, time(18, 0))

        from datetime import timedelta
        pvr_morning_show_tomorrow = Show(baahubali, pvr_screen1, today + timedelta(days=1), time(9, 0))

        # Attach shows to screens
        inox_screen1.add_show(inox_morning_show_today)
        inox_screen1.add_show(inox_afternoon_show_today)
        inox_screen1.add_show(inox_evening_show_today)
        pvr_screen1.add_show(pvr_morning_show_tomorrow)

    def user_flow(self):
        # User enters system
        user = User("U1", "Shrayansh")
        print("User logged in: Shrayansh")

        # 1. User selects city
        selected_city = City.BANGALORE
        print("Selected City: " + str(selected_city))

        # 2. for specific date, Show movies running in city
        selected_date = date.today()
        print("Selected Date: " + str(selected_date))

        movies = self._theatre_controller.get_movies(selected_city, selected_date)
        print("Movies available:")
        for m in movies:
            print(" - " + m.get_name())

        # 3. User selects movie
        selected_movie = next(iter(movies))
        print("Selected Movie: " + selected_movie.get_name())

        # 4. Show theatres and show times in city
        theatres = self._theatre_controller.get_theatres(selected_city, selected_movie, selected_date)
        print("Theatres available:")
        for t in theatres:
            print(" - " + t.get_name())

        # 6. User selects theatre
        selected_theatre = theatres[0]
        print("Selected Theatre: " + selected_theatre.get_name())

        # 7. Show running shows for movie + date + theatre
        shows = self._theatre_controller.get_shows(selected_movie, selected_date, selected_theatre)

        print("Shows available:")
        for s in shows:
            print(" - " + str(s.get_start_time()))

        # 8. User selects show
        selected_show = shows[0]
        print("Selected Show Time: " + str(selected_show.get_start_time()))

        # 9. User selects seats
        selected_seats = [1, 2, 3]
        print("Selected Seats: " + str(selected_seats))

        # 10. Booking + Payment
        booking = self._booking_controller.create_booking(user, selected_show, selected_seats)

        print("BOOKING SUCCESSFUL")
        print("Booking ID: " + str(booking.get_booking_id()))

    def _create_seats(self):
        seats = []
        for i in range(1, 21):
            seats.append(Seat(i, SeatCategory.SILVER))
        return seats


def main():
    BookMyShowApp.main()


if __name__ == "__main__":
    main()
