from .living_things import LivingThings


class Fish(LivingThings):
    # Breathing Process is tightly coupled to the LivingThings(abstraction)
    def breathe(self):
        print("Fish: Breathes through gills; Lives in water; Respiratory system: 2 gills")
        print("Breathing Process: Absorbs Oxygen from the water and releases Carbon Dioxide.")
