from .living_things import LivingThings


# Step 4: Refined Abstractions (Concrete LivingThings)
class Fish(LivingThings):
    def __init__(self, breathing_process):
        super().__init__(breathing_process)

    def breathe(self):
        print("Fish: ", end="")
        self.breathing_process.breathe()
