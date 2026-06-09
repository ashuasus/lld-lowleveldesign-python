import itertools
from datetime import datetime
from interviewquestions.carrental.payment.payment_strategy import PaymentStrategy
from interviewquestions.carrental.payment.payment import Payment
from interviewquestions.carrental.payment.payment_mode import PaymentMode


class UPIPaymentStrategy(PaymentStrategy):
    _id_counter = itertools.count(9000)

    def process_payment(self, bill, payment_amount):
        payment = Payment(
            next(self._id_counter),
            bill.get_bill_id(),
            payment_amount,
            PaymentMode.UPI,
            datetime.now(),
        )
        bill.set_bill_paid(True)
        return payment
