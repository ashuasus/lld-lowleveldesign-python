# Context class - holds a reference to a strategy object
class Vehicle:
    def __init__(self, drive_strategy):
        self.drive_strategy = drive_strategy

    def drive(self):
        print("\n" + self.__class__.__name__ + ": ", end="")
        self.drive_strategy.drive()
