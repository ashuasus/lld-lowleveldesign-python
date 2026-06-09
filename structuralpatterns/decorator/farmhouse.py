from .base_pizza import BasePizza


# Step 2: Define the Concrete Component
class Farmhouse(BasePizza):
    def get_description(self):
        return "Farmhouse Pizza"

    def get_cost(self):
        return 300.0
