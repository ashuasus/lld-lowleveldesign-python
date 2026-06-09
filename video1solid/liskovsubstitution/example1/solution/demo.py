from .motor_cycle import MotorCycle
from .bicycle import Bicycle


# Usage of LSP-compliant design
def main():
    motor_cycle = MotorCycle("HeroHonda", 10)
    bicycle = Bicycle("Hercules", True, 10)

    # Works fine with MotorCycle - implements all Bike class behavior
    motor_cycle.turn_on_engine()
    motor_cycle.accelerate()
    motor_cycle.apply_brakes()
    motor_cycle.turn_off_engine()
    # Works fine with Bicycle - implements all Bike class behavior
    bicycle.accelerate()
    bicycle.apply_brakes()


if __name__ == "__main__":
    main()
