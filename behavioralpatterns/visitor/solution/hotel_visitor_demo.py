from .elements.standard_room import StandardRoom
from .elements.deluxe_room import DeluxeRoom
from .elements.suite_room import SuiteRoom
from .visitors.housekeeping_visitor import HousekeepingVisitor
from .visitors.room_service_visitor import RoomServiceVisitor
from .visitors.pricing_visitor import PricingVisitor


# Usage
def main():
    print("\n###### Visitor Design Pattern Demo ######")

    # Create different room types(elements) - Standard, Deluxe, Suite
    rooms = [
        StandardRoom("101"),
        DeluxeRoom("201", True),
        SuiteRoom("301", 3),
        StandardRoom("102"),
        DeluxeRoom("202", False)
    ]

    # Calling Visitors on elements
    print("\n==> Housekeeping Service")
    housekeeping = HousekeepingVisitor()
    for room in rooms:
        room.accept(housekeeping)

    print("\n==> Room Service")
    room_service = RoomServiceVisitor("Breakfast")
    rooms[0].accept(room_service)  # Deliver to standard room
    rooms[1].accept(room_service)  # Deliver to deluxe room
    rooms[2].accept(room_service)  # Deliver to suite

    print("\n==> Revenue Calculation")
    pricing = PricingVisitor()
    for room in rooms:
        room.accept(pricing)
    print("Total Revenue: Rs." + str(pricing.get_total_revenue()))


if __name__ == "__main__":
    main()
