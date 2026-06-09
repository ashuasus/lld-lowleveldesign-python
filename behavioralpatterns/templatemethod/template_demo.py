from .bank_transfer import BankTransfer
from .merchant_payment import MerchantPayment


# Client class
def main():
    print("###### Template Method Design Pattern ######")

    # Bank Transfer
    print("===== Bank Transfer =====")
    bank_transfer = BankTransfer()
    bank_transfer.send_money()  # Template method
    bank_transfer.log_transaction()  # Common method

    # Merchant Payment
    print("===== Merchant Payment =====")
    merchant_payment = MerchantPayment()
    merchant_payment.send_money()  # Template method
    merchant_payment.log_transaction()  # Common method


if __name__ == "__main__":
    main()
