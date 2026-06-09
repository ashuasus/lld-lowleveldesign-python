from .motor_cycle import MotorCycle
from .bicycle import Bicycle


# Usage example - demonstrates the LSP violations
def main():
    motor_cycle = MotorCycle("HeroHonda", 10)
    bicycle = Bicycle("Hercules", True, 10)

    # Works fine with MotorCycle - implements all Bike class behavior
    motor_cycle.turn_on_engine()
    motor_cycle.accelerate()
    motor_cycle.apply_brakes()
    motor_cycle.turn_off_engine()
    # Client expects to be able to see the same behavior with Bicycle
    bicycle.turn_on_engine()  # fails to implement Bike class behavior
    bicycle.accelerate()
    bicycle.apply_brakes()
    bicycle.turn_off_engine()  # fails to implement Bike class behavior


if __name__ == "__main__":
    main()
