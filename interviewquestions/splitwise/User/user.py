from ..user_expense_balance_sheet import UserExpenseBalanceSheet


class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.user_expense_balance_sheet = UserExpenseBalanceSheet()

    def get_user_id(self):
        return self.user_id

    def get_user_expense_balance_sheet(self):
        return self.user_expense_balance_sheet
