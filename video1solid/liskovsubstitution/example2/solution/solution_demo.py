from .vehicle import Vehicle
from .engine_vehicle import EngineVehicle
from .motor_cycle import MotorCycle
from .car import Car
from .bicycle import Bicycle


def main():
    vehicle_list = [MotorCycle(), Car(), Bicycle()]
    for vehicle in vehicle_list:
        print(str(vehicle.get_number_of_wheels()))
    vehicle_list2 = [MotorCycle(), Car()]
    # vehicle_list2.append(Bicycle())  # would break type expectations
    for vehicle in vehicle_list2:
        pass
        # vehicle.has_engine()  # not safe without type check


if __name__ == "__main__":
    main()
