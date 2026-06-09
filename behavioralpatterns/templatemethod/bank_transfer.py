from .payment_flow import PaymentFlow


# Concrete class
class BankTransfer(PaymentFlow):
    def validate_request(self):
        print("[+] Specific Validation Logic for Bank Transfer")

    def debit_amount(self):
        print("[+] Specific Debit Amount Logic for Bank Transfer")

    def calculate_fees(self):
        print("[+] Specific Fee Calculation Logic for Bank Transfer. 0% Fees is applied.")

    def credit_amount(self):
        print("[+] Specific Credit Amount Logic for Bank Transfer. Full amount is credited.")
