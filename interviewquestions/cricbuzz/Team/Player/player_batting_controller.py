from collections import deque
from .player_details import PlayerDetails


class PlayerBattingController:

    def __init__(self, playing11):
        self.yet_to_play = deque(playing11)
        self.striker: PlayerDetails = None
        self.non_striker: PlayerDetails = None

    def get_next_player(self):
        if not self.yet_to_play:
            raise Exception()

        if self.striker is None:
            self.striker = self.yet_to_play.popleft()

        if self.non_striker is None:
            self.non_striker = self.yet_to_play.popleft()

    def get_striker(self) -> PlayerDetails:
        return self.striker

    def set_striker(self, player_details: PlayerDetails):
        self.striker = player_details

    def get_non_striker(self) -> PlayerDetails:
        return self.non_striker

    def set_non_striker(self, player_details: PlayerDetails):
        self.non_striker = player_details
