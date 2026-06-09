from .drive_strategy import DriveStrategy


# Concrete strategy for normal drive mode
class NormalDrive(DriveStrategy):
    def drive(self):
        print("Driving Capability: Normal")
