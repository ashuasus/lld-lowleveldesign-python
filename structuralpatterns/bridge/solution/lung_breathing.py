from .breathing_process import BreathingProcess


# Step 2: Concrete Implementor (various breathing processes)
class LungBreathing(BreathingProcess):
    def breathe(self):
        print("Breathing through lungs.")
