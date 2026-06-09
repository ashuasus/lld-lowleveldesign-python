from .over_details import OverDetails
from ..match_type import MatchType


class InningDetails:

    def __init__(self, batting_team, bowling_team, match_type: MatchType):
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.match_type = match_type
        self.overs = []

    def start(self, runs_to_win: int):
        # set batting players
        try:
            self.batting_team.choose_next_bats_man()
        except Exception:
            pass

        no_of_overs = self.match_type.no_of_overs()
        for over_number in range(1, no_of_overs + 1):
            # chooseBowler
            self.bowling_team.choose_next_bowler(self.match_type.max_over_count_bowlers())

            over = OverDetails(over_number, self.bowling_team.get_current_bowler())
            self.overs.append(over)
            try:
                won = over.start_over(self.batting_team, self.bowling_team, runs_to_win)
                if won:
                    break
            except Exception:
                break

            # swap striker and non striker
            temp = self.batting_team.get_striker()
            self.batting_team.set_striker(self.batting_team.get_non_striker())
            self.batting_team.set_non_striker(temp)

    def get_total_runs(self) -> int:
        return self.batting_team.get_total_runs()
