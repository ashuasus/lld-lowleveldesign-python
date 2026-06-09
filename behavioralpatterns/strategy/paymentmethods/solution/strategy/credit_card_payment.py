from .payment_strategy import PaymentStrategy


# Concrete strategy - for credit card payment
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self._card_number = card_number

    def pay(self, amount):
        print("Paid $" + str(amount) + " using credit card ending in " + self._card_number[-4:])
