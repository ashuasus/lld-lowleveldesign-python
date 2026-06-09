from ..Expense.expense_controller import ExpenseController


class Group:
    def __init__(self):
        self.group_id = None
        self.group_name = None
        self.group_members = []
        self.expense_list = []
        self.expense_controller = ExpenseController()

    def add_member(self, member):
        self.group_members.append(member)

    def get_group_id(self):
        return self.group_id

    def set_group_id(self, group_id):
        self.group_id = group_id

    def set_group_name(self, group_name):
        self.group_name = group_name

    def create_expense(self, expense_id, description, expense_amount, split_details, split_type, paid_by_user):
        expense = self.expense_controller.create_expense(expense_id, description, expense_amount, split_details, split_type, paid_by_user)
        self.expense_list.append(expense)
        return expense
