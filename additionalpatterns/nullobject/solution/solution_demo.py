from .vehicle_factory import VehicleFactory
from ..car import Car
from ..bike import Bike


def main():
    print("\n##### Null Object Pattern: Solution Demo #####")

    car = VehicleFactory.get_vehicle("car")
    print_vehicle_details(car)
    test_drive(car)

    bike = VehicleFactory.get_vehicle("bike")
    print_vehicle_details(bike)
    test_drive(car)

    null_vehicle = VehicleFactory.get_vehicle("null")
    print_vehicle_details(null_vehicle)
    test_drive(null_vehicle)


def print_vehicle_details(vehicle):
    if isinstance(vehicle, Car):
        print("\n[+] Vehicle Details: ", end="")
        print(vehicle.__class__.__name__ + " [Model=" + vehicle.get_model()
              + ", Color=" + vehicle.get_color() + ", Seating Capacity=" + str(vehicle.get_seating_capacity())
              + ", Fuel Tank Capacity=" + str(vehicle.get_fuel_tank_capacity()) + "]")
    if isinstance(vehicle, Bike):
        print("\n[+] Vehicle Details: ", end="")
        print(vehicle.__class__.__name__ + " [Model=" + vehicle.get_model()
              + ", Color=" + vehicle.get_color() + ", Fuel Tank Capacity=" + str(vehicle.get_fuel_tank_capacity()) + "]")


def test_drive(vehicle):
    vehicle.start()
    vehicle.stop()


if __name__ == "__main__":
    main()
