from .User.user import User
from .User.user_controller import UserController
from .Group.group_controller import GroupController
from .balance_sheet_controller import BalanceSheetController
from .Expense.expense_split_type import ExpenseSplitType
from .Expense.Split.split import Split


class Splitwise:
    def __init__(self):
        self.user_controller = UserController()
        self.group_controller = GroupController()
        self.balance_sheet_controller = BalanceSheetController()

    def demo(self):
        self.setup_user_and_group()

        # Step1: add members to the group
        group = self.group_controller.get_group("G1001")
        group.add_member(self.user_controller.get_user("U2001"))
        group.add_member(self.user_controller.get_user("U3001"))

        # Step2. create an expense inside a group
        splits = []
        split1 = Split(self.user_controller.get_user("U1001"), 300)
        split2 = Split(self.user_controller.get_user("U2001"), 300)
        split3 = Split(self.user_controller.get_user("U3001"), 300)
        splits.append(split1)
        splits.append(split2)
        splits.append(split3)
        group.create_expense("Exp1001", "Breakfast", 900, splits, ExpenseSplitType.EQUAL, self.user_controller.get_user("U1001"))

        splits2 = []
        splits2_1 = Split(self.user_controller.get_user("U1001"), 400)
        splits2_2 = Split(self.user_controller.get_user("U2001"), 100)
        splits2.append(splits2_1)
        splits2.append(splits2_2)
        group.create_expense("Exp1002", "Lunch", 500, splits2, ExpenseSplitType.UNEQUAL, self.user_controller.get_user("U2001"))

        for user in self.user_controller.get_all_users():
            self.balance_sheet_controller.show_balance_sheet_of_user(user)

    def setup_user_and_group(self):
        # onboard user to splitwise app
        self._add_users_to_splitwise_app()

        # create a group by user1
        user1 = self.user_controller.get_user("U1001")
        self.group_controller.create_new_group("G1001", "Outing with Friends", user1)

    def _add_users_to_splitwise_app(self):
        user1 = User("U1001", "User1")
        user2 = User("U2001", "User2")
        user3 = User("U3001", "User3")

        self.user_controller.add_user(user1)
        self.user_controller.add_user(user2)
        self.user_controller.add_user(user3)
