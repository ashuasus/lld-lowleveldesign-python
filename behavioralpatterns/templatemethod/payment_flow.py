from abc import ABC, abstractmethod


# Abstract class
class PaymentFlow(ABC):
    # Abstract methods - these methods are implemented by the subclasses.
    @abstractmethod
    def validate_request(self):
        pass

    @abstractmethod
    def debit_amount(self):
        pass

    @abstractmethod
    def calculate_fees(self):
        pass

    @abstractmethod
    def credit_amount(self):
        pass

    # Template method: which defines the order of steps to execute the task.
    def send_money(self):
        # step 1
        self.validate_request()
        # step 2
        self.debit_amount()
        # step 3
        self.calculate_fees()
        # step 4
        self.credit_amount()

    # Hook method: which can be overridden by the subclasses.
    def requires_otp_authentication(self):
        return False  # Default: authentication not required

    # Common method: All subclasses share this common functionality.
    def log_transaction(self):
        print("Transaction Completed!")
