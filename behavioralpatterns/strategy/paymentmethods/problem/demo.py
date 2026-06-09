from .payment_processor import PaymentProcessor


def main():
    print("Payment Processor: Problem Demo")
    processor = PaymentProcessor()
    processor.process_payment("credit_card", 100)
    processor.process_payment("paypal", 200)
    processor.process_payment("net_banking", 300)
    processor.process_payment("cash", 400)


if __name__ == "__main__":
    main()
