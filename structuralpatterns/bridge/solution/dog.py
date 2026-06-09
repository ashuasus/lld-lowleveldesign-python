from .living_things import LivingThings


# Step 4: Refined Abstractions (Concrete LivingThings)
class Dog(LivingThings):
    def __init__(self, breathing_process):
        super().__init__(breathing_process)

    def breathe(self):
        print("Dog: ", end="")
        self.breathing_process.breathe()  # Operation implemented by Implementor - defines the "HOW"
