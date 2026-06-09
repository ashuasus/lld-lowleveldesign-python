from behavioralpatterns.strategy.paymentmethods.solution.strategy.payment_strategy import PaymentStrategy


class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paid ${amount} using UPI ID {self.upi_id}")
