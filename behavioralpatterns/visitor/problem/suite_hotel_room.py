# Bloated Element class with multiple operations
class SuiteHotelRoom:
    def __init__(self, room_number, number_of_rooms):
        self._room_number = room_number
        self._number_of_rooms = number_of_rooms

    def clean(self):
        print("Housekeeping: Cleaning suite " +
              self._room_number + " with " +
              self._number_of_rooms + " rooms (90 minutes)")

    def deliver_room_service(self, order_details):
        print("Room Service: VIP delivery of " + order_details +
              " to suite " + self._room_number +
              " with full dining setup")

    def calculate_price(self):
        print("Pricing: Suite " + self._room_number +
              " - Rs. 2000/night")
        return 500.0

    # many more operations can come over the time
