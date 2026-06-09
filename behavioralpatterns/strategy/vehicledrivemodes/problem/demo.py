from .vehicle import Vehicle
from .sports_vehicle import SportsVehicle
from .off_road_vehicle import OffRoadVehicle
from .passenger_vehicle import PassengerVehicle


def main():
    print("Vehicle Drive Modes: Problem Demo")
    vehicle = Vehicle()

    # Sports vehicle - sports drive mode
    vehicle = SportsVehicle()
    vehicle.drive()

    # Off-road vehicle - sports drive mode
    vehicle = OffRoadVehicle()
    vehicle.drive()

    # Passenger vehicle - normal drive mode
    vehicle = PassengerVehicle()
    vehicle.drive()


if __name__ == "__main__":
    main()
