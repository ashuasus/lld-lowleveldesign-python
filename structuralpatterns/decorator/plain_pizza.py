from .base_pizza import BasePizza


# Step 2: Define the Concrete Component
class PlainPizza(BasePizza):
    def get_description(self):
        return "Plain Pizza"

    def get_cost(self):
        return 200.00
