from interviewquestions.parking_lot.payment.payment import Payment


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"UPI paid: {amount}")
        return True
