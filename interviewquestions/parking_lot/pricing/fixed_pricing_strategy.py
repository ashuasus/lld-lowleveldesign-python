from .pricing_strategy import PricingStrategy


class FixedPricingStrategy(PricingStrategy):
    def calculate(self, ticket):
        return 100
