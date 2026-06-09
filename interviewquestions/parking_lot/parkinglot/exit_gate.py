class ExitGate:
    def __init__(self, cost_computation):
        self._cost_computation = cost_computation

    def complete_exit(self, building, ticket, payment):
        amount = self._calculate_price(ticket)
        success = payment.pay(amount)
        if not success:
            raise RuntimeError("Payment failed. Exit denied.")
        building.release(ticket)
        print("Exit successful. Gate opened.")

    def _calculate_price(self, ticket):
        return self._cost_computation.compute(ticket)
