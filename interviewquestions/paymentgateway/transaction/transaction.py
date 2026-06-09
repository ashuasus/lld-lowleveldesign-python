from .transaction_status import TransactionStatus


class Transaction:

    def __init__(self):
        self.txn_id: int = 0
        self.amount: int = 0
        self.sender_id: int = 0
        self.receiver_id: int = 0
        self.debit_instrument_id: int = 0
        self.credit_instrument_id: int = 0
        self.status: TransactionStatus = None

    def get_txn_id(self) -> int:
        return self.txn_id

    def set_txn_id(self, txn_id: int):
        self.txn_id = txn_id

    def get_amount(self) -> int:
        return self.amount

    def set_amount(self, amount: int):
        self.amount = amount

    def get_sender_id(self) -> int:
        return self.sender_id

    def set_sender_id(self, sender_id: int):
        self.sender_id = sender_id

    def get_receiver_id(self) -> int:
        return self.receiver_id

    def set_receiver_id(self, receiver_id: int):
        self.receiver_id = receiver_id

    def get_debit_instrument_id(self) -> int:
        return self.debit_instrument_id

    def set_debit_instrument_id(self, debit_instrument_id: int):
        self.debit_instrument_id = debit_instrument_id

    def get_credit_instrument_id(self) -> int:
        return self.credit_instrument_id

    def set_credit_instrument_id(self, credit_instrument_id: int):
        self.credit_instrument_id = credit_instrument_id

    def get_status(self) -> TransactionStatus:
        return self.status

    def set_status(self, status: TransactionStatus):
        self.status = status
