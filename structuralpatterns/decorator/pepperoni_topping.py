from .topping_decorator import ToppingDecorator


# Step 4: Define the Concrete Decorators
class PepperoniTopping(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + " + Pepperoni"

    def get_cost(self):
        return self.pizza.get_cost() + 50
