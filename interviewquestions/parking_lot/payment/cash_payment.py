from .payment import Payment


class CashPayment(Payment):
    def pay(self, amount):
        print("Cash paid: " + str(amount))
        return True
