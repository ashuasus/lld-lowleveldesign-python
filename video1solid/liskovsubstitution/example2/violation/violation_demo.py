from .vehicle import Vehicle
from .motor_cycle import MotorCycle
from .car import Car
from .bicycle import Bicycle


# Usage example - Violation of Liskov Substitution
def main():
    # Happy Flow
    vehicle_list = [MotorCycle(), Car()]
    for vehicle in vehicle_list:
        print(str(vehicle.has_engine()))
    # Add Bicycle - Violation of LSP
    vehicle_list2 = [MotorCycle(), Car(), Bicycle()]
    for vehicle in vehicle_list2:
        print(str(vehicle.has_engine()))  # throws NPE equivalent


if __name__ == "__main__":
    main()
