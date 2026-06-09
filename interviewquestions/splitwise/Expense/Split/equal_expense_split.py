from .expense_split import ExpenseSplit


class EqualExpenseSplit(ExpenseSplit):
    def validate_split_request(self, split_list, total_amount):
        # validate total amount in splits of each user is equal and overall equals to totalAmount or not
        amount_should_be_present = total_amount / len(split_list)
        for split in split_list:
            if split.get_amount_owe() != amount_should_be_present:
                pass  # throw exception
