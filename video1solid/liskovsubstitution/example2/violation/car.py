from .vehicle import Vehicle


class Car(Vehicle):
    def get_number_of_wheels(self):
        return 4

    def get_specifications(self):
        return "Car has " + str(self.get_number_of_wheels()) + " wheels and has engine: " + str(self.has_engine())
