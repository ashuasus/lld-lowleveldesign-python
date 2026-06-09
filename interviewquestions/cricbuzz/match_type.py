from abc import ABC, abstractmethod


class MatchType(ABC):

    @abstractmethod
    def no_of_overs(self) -> int:
        pass

    @abstractmethod
    def max_over_count_bowlers(self) -> int:
        pass
