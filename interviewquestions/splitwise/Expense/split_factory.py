from .expense_split_type import ExpenseSplitType
from .Split.equal_expense_split import EqualExpenseSplit
from .Split.unequal_expense_split import UnequalExpenseSplit
from .Split.percentage_expense_split import PercentageExpenseSplit


class SplitFactory:
    @staticmethod
    def get_split_object(split_type):
        if split_type == ExpenseSplitType.EQUAL:
            return EqualExpenseSplit()
        elif split_type == ExpenseSplitType.UNEQUAL:
            return UnequalExpenseSplit()
        elif split_type == ExpenseSplitType.PERCENTAGE:
            return PercentageExpenseSplit()
        return None
