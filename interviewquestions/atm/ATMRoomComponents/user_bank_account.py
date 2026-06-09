class UserBankAccount:
    def __init__(self):
        self.balance = 0

    def withdrawal_balance(self, amount):
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance
