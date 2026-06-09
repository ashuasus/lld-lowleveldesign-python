class Card:
    PIN_NUMBER = 112211

    def __init__(self):
        self.card_number = 0
        self.cvv = 0
        self.expiry_date = 0
        self.holder_name = 0
        self.bank_account = None

    def is_correct_pin_entered(self, pin):
        return pin == Card.PIN_NUMBER

    def get_bank_balance(self):
        return self.bank_account.balance

    def deduct_bank_balance(self, amount):
        self.bank_account.withdrawal_balance(amount)

    def set_bank_account(self, bank_account):
        self.bank_account = bank_account
