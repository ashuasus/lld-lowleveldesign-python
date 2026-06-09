from datetime import datetime


class Payment:
    def __init__(self, payment_id, bill_id, amount_paid, payment_mode, payment_date):
        self._payment_id = payment_id
        self._bill_id = bill_id
        self._amount_paid = amount_paid
        self._payment_mode = payment_mode
        self._payment_date = payment_date

    def get_payment_id(self):
        return self._payment_id

    def get_bill_id(self):
        return self._bill_id

    def get_amount_paid(self):
        return self._amount_paid

    def get_payment_mode(self):
        return self._payment_mode

    def get_payment_date(self):
        return self._payment_date
