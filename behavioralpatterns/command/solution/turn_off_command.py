from .i_command import ICommand


# Concrete Command
class TurnOffCommand(ICommand):
    def __init__(self, ac):
        self.ac = ac
        self.previous_state = False

    def execute(self):
        self.previous_state = self.ac.is_on
        self.ac.turn_off()

    def undo(self):
        print("Undo: Turn Off command. ", end="")
        if self.previous_state:
            self.ac.turn_on()
