from .payment_strategy import PaymentStrategy


# Concrete strategy - for PayPal payment
class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self._email = email

    def pay(self, amount):
        print("Paid $" + str(amount) + " using PayPal account " + self._email)
