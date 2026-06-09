from .transaction import Transaction
from .transaction_do import TransactionDO
from .transaction_service import TransactionService


class TransactionController:

    def __init__(self):
        self.txn_service = TransactionService()

    def make_payment(self, txn_do: TransactionDO) -> TransactionDO:
        return self.txn_service.make_payment(txn_do)

    def get_transaction_history(self, user_id: int) -> list:
        return self.txn_service.get_transaction_history(user_id)
