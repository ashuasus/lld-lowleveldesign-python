from .i_command import ICommand


# Concrete Commands
class TurnOnCommand(ICommand):
    def __init__(self, ac):
        self.ac = ac
        self.previous_state = False

    def execute(self):
        self.previous_state = self.ac.is_on
        self.ac.turn_on()

    def undo(self):
        print("Undo: Turn On command. ", end="")
        if not self.previous_state:
            self.ac.turn_off()
