from behavioralpatterns.strategy.vehicledrivemodes.solution.strategies.drive_strategy import DriveStrategy


class EVDrive(DriveStrategy):
    def drive(self):
        print("Driving Capability: Electric")
