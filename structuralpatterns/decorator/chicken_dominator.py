from .base_pizza import BasePizza


# Step 2: Define the Concrete Component
class ChickenDominator(BasePizza):
    def get_description(self):
        return "Chicken Dominator Pizza"

    def get_cost(self):
        return 500.0
