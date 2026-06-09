from abc import ABC, abstractmethod


class ExpenseSplit(ABC):
    @abstractmethod
    def validate_split_request(self, split_list, total_amount):
        pass
