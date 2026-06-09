from .topping_decorator import ToppingDecorator


# Step 4: Define the Concrete Decorators
class ExtraCheeseTopping(ToppingDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + " + Extra Cheese"

    def get_cost(self):
        return self.pizza.get_cost() + 20
