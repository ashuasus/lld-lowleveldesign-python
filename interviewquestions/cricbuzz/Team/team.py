from .Player.player_batting_controller import PlayerBattingController
from .Player.player_bowling_controller import PlayerBowlingController
from .Player.player_details import PlayerDetails


class Team:

    def __init__(self, team_name: str, playing11, bench: list, bowlers: list):
        self.team_name = team_name
        self.playing11 = playing11
        self.bench = bench
        self.batting_controller = PlayerBattingController(playing11)
        self.bowling_controller = PlayerBowlingController(bowlers)
        self.is_winner: bool = False

    def get_team_name(self) -> str:
        return self.team_name

    def choose_next_bats_man(self):
        self.batting_controller.get_next_player()

    def choose_next_bowler(self, max_over_count_per_bowler: int):
        self.bowling_controller.get_next_bowler(max_over_count_per_bowler)

    def get_striker(self) -> PlayerDetails:
        return self.batting_controller.get_striker()

    def set_striker(self, player: PlayerDetails):
        self.batting_controller.set_striker(player)

    def get_non_striker(self) -> PlayerDetails:
        return self.batting_controller.get_non_striker()

    def set_non_striker(self, player: PlayerDetails):
        self.batting_controller.set_non_striker(player)

    def get_current_bowler(self) -> PlayerDetails:
        return self.bowling_controller.get_current_bowler()

    def print_batting_score_card(self):
        for player_details in self.playing11:
            player_details.print_batting_score_card()

    def print_bowling_score_card(self):
        for player_details in self.playing11:
            if player_details.bowling_score_card.total_overs_count > 0:
                player_details.print_bowling_score_card()

    def get_total_runs(self) -> int:
        total_run = 0
        for player in self.playing11:
            total_run += player.batting_score_card.total_runs
        return total_run
