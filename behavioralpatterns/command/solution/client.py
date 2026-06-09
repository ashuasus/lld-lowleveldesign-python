from .air_conditioner import AirConditioner
from .remote_controller import RemoteController
from .turn_on_command import TurnOnCommand
from .turn_off_command import TurnOffCommand
from .set_temperature_command import SetTemperatureCommand


# Client - Demonstration
def main():
    print("##### Command Pattern: Solution Demo #####")

    # Create Receiver
    air_conditioner = AirConditioner()

    # Create Invoker
    remote_obj = RemoteController()

    # Execute Commands
    remote_obj.set_command(TurnOnCommand(air_conditioner))
    remote_obj.press_button()
    remote_obj.set_command(SetTemperatureCommand(air_conditioner, 25))
    remote_obj.press_button()
    remote_obj.set_command(SetTemperatureCommand(air_conditioner, 18))
    remote_obj.press_button()
    remote_obj.set_command(TurnOffCommand(air_conditioner))
    remote_obj.press_button()

    # Undo Command
    remote_obj.undo()  # Undo: Turn Off command => AC is now on

    # Undo Command
    remote_obj.undo()  # Undo: Set Temperature Command. AC temperature is now 25°C

    # Undo Command
    remote_obj.undo()  # Undo: Set Temperature Command. AC temperature is now 0°C

    # Undo Command
    remote_obj.undo()  # Undo: Turn On command => AC is now off


if __name__ == "__main__":
    main()
