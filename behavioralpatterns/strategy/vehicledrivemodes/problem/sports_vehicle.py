from .vehicle import Vehicle


class SportsVehicle(Vehicle):
    # Overriding the drive method to provide specific behavior for sports vehicles
    def drive(self):
        print("\n" + self.__class__.__name__ + ": ", end="")
        print("Driving Capability: Sports")
