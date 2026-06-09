# A simple payment processor class - bloated with payment logic
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            # x lines of credit card logic
            print("Paid $" + str(amount) + " using credit card")
        elif payment_type == "paypal":
            # y lines of PayPal logic
            print("Paid $" + str(amount) + " using PayPal")
        elif payment_type == "net_banking":
            # z lines of bank transfer logic
            print("Paid $" + str(amount) + " using bank transfer")
        elif payment_type == "cash":
            # 10 lines of cash on delivery logic
            print("Paid $" + str(amount) + " using cash")
        else:
            raise ValueError("Unexpected value: " + payment_type)
        # Adding another payment method(crypto) requires modifying this class
        # This keeps growing with each new payment method
        # bad design
