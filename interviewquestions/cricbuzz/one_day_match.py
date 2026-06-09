from .match_type import MatchType


class OneDayMatch(MatchType):

    def no_of_overs(self) -> int:
        return 50

    def max_over_count_bowlers(self) -> int:
        return 10
