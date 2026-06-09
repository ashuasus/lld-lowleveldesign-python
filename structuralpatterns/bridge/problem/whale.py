from .living_things import LivingThings


class Whale(LivingThings):
    # Breathing Process is tightly coupled to the LivingThings(abstraction)
    def breathe(self):
        print("Whale: Breathes through lungs; Lives in water; Respiratory system: 2 lungs")
        print("Breathing Process: Inhales Oxygen from the water and Exhales Carbon Dioxide")
