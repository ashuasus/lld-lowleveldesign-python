from .person import Person
from .player_type import PlayerType
from .Score.batting_score_card import BattingScoreCard
from .Score.bowling_score_card import BowlingScoreCard


class PlayerDetails:

    def __init__(self, person: Person, player_type: PlayerType):
        self.person = person
        self.player_type = player_type
        self.batting_score_card = BattingScoreCard()
        self.bowling_score_card = BowlingScoreCard()

    def print_batting_score_card(self):
        out_by = (self.batting_score_card.wicket_details.taken_by.person.name
                  if self.batting_score_card.wicket_details is not None
                  else "notout")
        print(f"PlayerName: {self.person.name} -- totalRuns: {self.batting_score_card.total_runs}"
              f" -- totalBallsPlayed: {self.batting_score_card.total_balls_played}"
              f" -- 4s: {self.batting_score_card.total_fours}"
              f" -- 6s: {self.batting_score_card.total_six}"
              f" -- outby: {out_by}")

    def print_bowling_score_card(self):
        print(f"PlayerName: {self.person.name}"
              f" -- totalOversThrown: {self.bowling_score_card.total_overs_count}"
              f" -- totalRunsGiven: {self.bowling_score_card.runs_given}"
              f" -- WicketsTaken: {self.bowling_score_card.wickets_taken}")
