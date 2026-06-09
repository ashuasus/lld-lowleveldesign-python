class Vehicle:
    def drive(self):
        print("\n" + self.__class__.__name__ + ": ", end="")
        print("Driving Capability: Normal")
