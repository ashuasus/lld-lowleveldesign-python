class Bulb:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Bulb is on")

    def turn_off(self):
        self.is_on = False
        print("Bulb is off")
