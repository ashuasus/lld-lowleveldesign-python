class Expense:
    def __init__(self, expense_id, expense_amount, description, paid_by_user, split_type, split_details):
        self.expense_id = expense_id
        self.description = description
        self.expense_amount = expense_amount
        self.paid_by_user = paid_by_user
        self.split_type = split_type
        self.split_details = list(split_details)
