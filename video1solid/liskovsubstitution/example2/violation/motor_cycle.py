from .vehicle import Vehicle


class MotorCycle(Vehicle):
    def get_specifications(self):
        return "MotorCycle has " + str(self.get_number_of_wheels()) + " wheels and has engine: " + str(self.has_engine())
