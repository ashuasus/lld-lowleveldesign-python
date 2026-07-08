from .payment_mode import PaymentMode


class CardPaymentMode(PaymentMode):

    def make_payment(self) -> bool:
        print("Payment done via Card.")
        return True
