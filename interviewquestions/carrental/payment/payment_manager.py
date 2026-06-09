class PaymentManager:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy
        self._payments = {}

    def make_payment(self, bill, payment_amount):
        payment = self._payment_strategy.process_payment(bill, payment_amount)
        self._payments[payment.get_payment_id()] = payment
        return payment

    def get_payments_for_bill(self, bill_id):
        return [p for p in self._payments.values() if p.get_bill_id() == bill_id]

    def get_payment(self, payment_id):
        return self._payments.get(payment_id)

    def set_payment_strategy(self, payment_strategy):
        self._payment_strategy = payment_strategy
