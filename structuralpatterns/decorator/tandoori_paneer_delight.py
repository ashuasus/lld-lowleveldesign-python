from .base_pizza import BasePizza


# Step 2: Define the Concrete Component
class TandooriPaneerDelight(BasePizza):
    def get_description(self):
        return "Tandoori Paneer Delight Pizza"

    def get_cost(self):
        return 400.0
