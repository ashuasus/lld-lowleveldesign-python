from .payment_flow import PaymentFlow


# Concrete class
class MerchantPayment(PaymentFlow):
    def validate_request(self):
        print("[+] Specific Validation Logic for Merchant Payment")

    def debit_amount(self):
        if self.requires_otp_authentication():
            print("[+] Perform OTP Authentication.")
        print("[+] Specific Debit Amount Logic for Merchant Payment")

    def calculate_fees(self):
        print("[+] Specific Fee Calculation Logic for Merchant Payment. 2% Fees is applied.")

    def credit_amount(self):
        print("[+] Specific Credit Amount Logic for Merchant Payment. Remaining amount is credited.")

    # Hook method - overridden by subclass
    def requires_otp_authentication(self):
        return True
