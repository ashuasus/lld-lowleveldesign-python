class Bill:
    def __init__(self, bill_id, reservation_id, total_bill_amount):
        self._bill_id = bill_id
        self._reservation_id = reservation_id
        self._total_bill_amount = total_bill_amount
        self._bill_paid = False

    def get_bill_id(self):
        return self._bill_id

    def get_reservation_id(self):
        return self._reservation_id

    def get_total_bill_amount(self):
        return self._total_bill_amount

    def is_bill_paid(self):
        return self._bill_paid

    def set_bill_paid(self, bill_paid):
        self._bill_paid = bill_paid
