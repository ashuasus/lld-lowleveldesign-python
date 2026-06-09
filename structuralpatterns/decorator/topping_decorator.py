from abc import ABC
from .base_pizza import BasePizza


# Step 3: Define the Abstract Base Decorator
class ToppingDecorator(BasePizza, ABC):
    def __init__(self, pizza):
        self.pizza = pizza
