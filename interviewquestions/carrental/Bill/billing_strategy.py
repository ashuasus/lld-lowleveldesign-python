from abc import ABC, abstractmethod


class BillingStrategy(ABC):
    @abstractmethod
    def generate_bill(self, reservation):
        pass
