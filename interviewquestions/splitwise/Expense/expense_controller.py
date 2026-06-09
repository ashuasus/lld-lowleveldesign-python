from ..balance_sheet_controller import BalanceSheetController
from .expense import Expense
from .split_factory import SplitFactory


class ExpenseController:
    def __init__(self):
        self.balance_sheet_controller = BalanceSheetController()

    def create_expense(self, expense_id, description, expense_amount, split_details, split_type, paid_by_user):
        expense_split = SplitFactory.get_split_object(split_type)
        expense_split.validate_split_request(split_details, expense_amount)

        expense = Expense(expense_id, expense_amount, description, paid_by_user, split_type, split_details)
        self.balance_sheet_controller.update_user_expense_balance_sheet(paid_by_user, split_details, expense_amount)
        return expense
