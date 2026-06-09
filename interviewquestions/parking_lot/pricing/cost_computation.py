class CostComputation:
    def __init__(self, pricing_strategy):
        self._pricing_strategy = pricing_strategy

    def compute(self, ticket):
        return self._pricing_strategy.calculate(ticket)
