# Invoker - with undo functionality
class RemoteController:
    def __init__(self):
        self.command = None
        self.command_history = []

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()
        self.command_history.append(self.command)

    def undo(self):
        if self.command_history:
            last_command = self.command_history.pop()
            last_command.undo()
