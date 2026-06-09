class BillManager:
    def __init__(self, billing_strategy):
        self._billing_strategy = billing_strategy
        self._bills = {}

    def generate_bill(self, reservation):
        bill = self._billing_strategy.generate_bill(reservation)
        self._bills[bill.get_bill_id()] = bill
        return bill

    def get_bill(self, bill_id):
        return self._bills.get(bill_id)

    def set_billing_strategy(self, billing_strategy):
        self._billing_strategy = billing_strategy
