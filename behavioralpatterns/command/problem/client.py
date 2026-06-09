from .air_conditioner import AirConditioner
from .bulb import Bulb


def main():
    print("##### Command Pattern: Problem Demo #####")

    # Device: Air Conditioner Commands
    air_conditioner = AirConditioner()
    air_conditioner.turn_on()
    air_conditioner.set_temperature(25)
    air_conditioner.turn_off()

    # Device: Bulb Commands
    bulb = Bulb()
    bulb.turn_on()
    bulb.turn_off()


if __name__ == "__main__":
    main()
