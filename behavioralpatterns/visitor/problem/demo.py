from .suite_hotel_room import SuiteHotelRoom


# Usage
def main():
    print("##### Visitor Pattern: Problem Demo #####")
    suite = SuiteHotelRoom("301", "2")
    suite.clean()
    suite.deliver_room_service("Breakfast")
    suite.calculate_price()


if __name__ == "__main__":
    main()
