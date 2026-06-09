from .breathing_process import BreathingProcess


# Step 2: Concrete Implementor (various breathing processes)
class Photosynthesis(BreathingProcess):
    def breathe(self):
        print("Breathing through process of photosynthesis. Releases Oxygen through leaves.")
