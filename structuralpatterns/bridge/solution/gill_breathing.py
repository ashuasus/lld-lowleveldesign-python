from .breathing_process import BreathingProcess


# Step 2: Concrete Implementor (various breathing processes)
class GillBreathing(BreathingProcess):
    def breathe(self):
        print("Breathing through gills.")
