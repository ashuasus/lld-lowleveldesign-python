import random
from .Inning.inning_details import InningDetails
from .Team.team import Team
from .match_type import MatchType


class Match:

    def __init__(self, team_a: Team, team_b: Team, match_date, venue: str, match_type: MatchType):
        self.team_a = team_a
        self.team_b = team_b
        self.match_date = match_date
        self.venue = venue
        self.match_type = match_type
        self.toss_winner: Team = None
        self.innings = [None, None]

    def start_match(self):
        # 1. Toss
        self.toss_winner = self._toss(self.team_a, self.team_b)

        # start The Inning, there are 2 innings in a match
        for inning in range(1, 3):
            # assuming here that tossWinner batFirst
            if inning == 1:
                batting_team = self.toss_winner
                bowling_team = self.team_b if self.toss_winner.get_team_name() == self.team_a.get_team_name() else self.team_a
                inning_details = InningDetails(batting_team, bowling_team, self.match_type)
                inning_details.start(-1)
            else:
                bowling_team = self.toss_winner
                batting_team = self.team_b if self.toss_winner.get_team_name() == self.team_a.get_team_name() else self.team_a
                inning_details = InningDetails(batting_team, bowling_team, self.match_type)
                inning_details.start(self.innings[0].get_total_runs())
                if bowling_team.get_total_runs() > batting_team.get_total_runs():
                    bowling_team.is_winner = True

            self.innings[inning - 1] = inning_details

            # print inning details
            print()
            print(f"INNING {inning} -- total Run: {batting_team.get_total_runs()}")
            print(f"---Batting ScoreCard : {batting_team.team_name}---")

            batting_team.print_batting_score_card()

            print()
            print(f"---Bowling ScoreCard : {bowling_team.team_name}---")
            bowling_team.print_bowling_score_card()

        print()
        if self.team_a.is_winner:
            print(f"---WINNER---{self.team_a.team_name}")
        else:
            print(f"---WINNER---{self.team_b.team_name}")

    def _toss(self, team_a: Team, team_b: Team) -> Team:
        # random function return value between 0 and 1
        if random.random() < 0.5:
            return team_a
        else:
            return team_b
