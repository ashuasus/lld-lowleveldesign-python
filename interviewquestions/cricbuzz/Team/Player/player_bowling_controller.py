from collections import deque
from .player_details import PlayerDetails


class PlayerBowlingController:

    def __init__(self, bowlers: list):
        self.bowlers_list = deque()
        self.bowler_vs_over_count: dict = {}
        self.current_bowler: PlayerDetails = None
        self._set_bowlers_list(bowlers)

    def _set_bowlers_list(self, bowlers_list: list):
        self.bowlers_list = deque()
        self.bowler_vs_over_count = {}
        for bowler in bowlers_list:
            self.bowlers_list.append(bowler)
            self.bowler_vs_over_count[bowler] = 0

    def get_next_bowler(self, max_over_count_per_bowler: int):
        player_details = self.bowlers_list.popleft()
        if self.bowler_vs_over_count[player_details] + 1 == max_over_count_per_bowler:
            self.current_bowler = player_details
        else:
            self.current_bowler = player_details
            self.bowlers_list.append(player_details)
            self.bowler_vs_over_count[player_details] = self.bowler_vs_over_count[player_details] + 1

    def get_current_bowler(self) -> PlayerDetails:
        return self.current_bowler
