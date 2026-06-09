from .living_things import LivingThings


class Tree(LivingThings):
    # Breathing Process is tightly coupled to the LivingThings(abstraction)
    def breathe(self):
        print("Tree: Breathes through leaves; Lives on land; Respiratory system: Leaves")
        print("Breathing Process: Inhales Carbon Dioxide and Exhales Oxygen as a result of photosynthesis.")
