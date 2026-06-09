# Context class - holds reference to a strategy object
class ShoppingCart:
    def __init__(self):
        self._payment_strategy = None

    def set_payment_strategy(self, strategy):
        self._payment_strategy = strategy

    def checkout(self, amount):
        print(self._payment_strategy.__class__.__name__ + ": ", end="")
        self._payment_strategy.pay(amount)
