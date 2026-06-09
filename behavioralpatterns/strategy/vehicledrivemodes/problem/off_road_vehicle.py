from .vehicle import Vehicle


class OffRoadVehicle(Vehicle):
    # Overriding the drive method to provide specific behavior
    def drive(self):
        print("\n" + self.__class__.__name__ + ": ", end="")
        print("Driving Capability: Sports")  # code duplication
