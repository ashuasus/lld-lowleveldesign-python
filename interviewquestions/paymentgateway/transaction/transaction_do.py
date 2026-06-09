class TransactionDO:
    def __init__(self, txn_id=0, sender_id=0, receiver_id=0,
                 debit_instrument_id=0, credit_instrument_id=0,
                 amount=0, status=None):
        self.txn_id = txn_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.debit_instrument_id = debit_instrument_id
        self.credit_instrument_id = credit_instrument_id
        self.amount = amount
        self.status = status
