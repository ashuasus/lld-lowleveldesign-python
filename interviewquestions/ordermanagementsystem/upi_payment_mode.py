from .payment_mode import PaymentMode


class UPIPaymentMode(PaymentMode):

    def make_payment(self) -> bool:
        print("Payment done via UPI.")
        return True
