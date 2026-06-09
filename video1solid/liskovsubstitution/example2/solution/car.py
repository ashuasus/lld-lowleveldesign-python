from .engine_vehicle import EngineVehicle


class Car(EngineVehicle):
    def get_number_of_wheels(self):
        return 4
