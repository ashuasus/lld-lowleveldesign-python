class AirConditioner:
    def __init__(self):
        self.is_on = False
        self.temperature = 0

    def turn_on(self):
        self.is_on = True
        print("Air conditioner is on")

    def turn_off(self):
        self.is_on = False
        print("Air conditioner is off")

    def set_temperature(self, temperature):
        self.temperature = temperature
        print("Air conditioner temperature set to " + str(temperature))
