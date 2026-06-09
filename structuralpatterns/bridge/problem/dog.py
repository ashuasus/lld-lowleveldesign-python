from .living_things import LivingThings


class Dog(LivingThings):
    # Breathing Process is tightly coupled to the LivingThings(abstraction)
    def breathe(self):
        print("Dog: Breathes through its nose; Lives on land; Respiratory system: 2 lungs")
        print("Breathing Process: Inhales Oxygen from the air and Exhales Carbon Dioxide.")
