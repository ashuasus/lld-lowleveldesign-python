from .drive_strategy import DriveStrategy


# Concrete strategy for sports drive mode
class SportsDrive(DriveStrategy):
    def drive(self):
        print("Driving Capability: Sports")
