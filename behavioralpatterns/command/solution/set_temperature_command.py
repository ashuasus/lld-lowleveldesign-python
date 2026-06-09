from .i_command import ICommand


# Concrete Command
class SetTemperatureCommand(ICommand):
    def __init__(self, ac, temperature):
        self.ac = ac
        self.new_temperature = temperature
        self.previous_temperature = 0

    def execute(self):
        self.previous_temperature = self.ac.get_temperature()
        self.ac.set_temperature(self.new_temperature)

    def undo(self):
        print("Undo: Set Temperature Command. ", end="")
        self.ac.set_temperature(self.previous_temperature)
