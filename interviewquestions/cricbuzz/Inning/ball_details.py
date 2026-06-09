import random
from .ball_type import BallType
from .run_type import RunType
from ..ScoreUpdater.bowling_score_updater import BowlingScoreUpdater
from ..ScoreUpdater.batting_score_updater import BattingScoreUpdater
from ..Team.wicket import Wicket
from ..Team.wicket_type import WicketType


class BallDetails:

    def __init__(self, ball_number: int):
        self.ball_number = ball_number
        self.ball_type: BallType = None
        self.run_type: RunType = None
        self.played_by = None
        self.bowled_by = None
        self.wicket: Wicket = None
        self.score_updater_observer_list = [
            BowlingScoreUpdater(),
            BattingScoreUpdater()
        ]

    def start_ball_delivery(self, batting_team, bowling_team, over):
        self.played_by = batting_team.get_striker()
        self.bowled_by = over.bowled_by
        # THROW BALL AND GET THE BALL TYPE, assuming here that ball type is always NORMAL
        self.ball_type = BallType.NORMAL

        # wicket or no wicket
        if self._is_wicket_taken():
            self.run_type = RunType.ZERO
            # considering only BOLD
            self.wicket = Wicket(WicketType.BOLD, bowling_team.get_current_bowler(), over, self)
            # making only striker out for now
            batting_team.set_striker(None)
        else:
            self.run_type = self._get_run_type()

            if self.run_type == RunType.ONE or self.run_type == RunType.THREE:
                # swap striker and non striker
                temp = batting_team.get_striker()
                batting_team.set_striker(batting_team.get_non_striker())
                batting_team.set_non_striker(temp)

        # update player scoreboard
        self._notify_updaters(self)

    def _notify_updaters(self, ball_details):
        for observer in self.score_updater_observer_list:
            observer.update(ball_details)

    def _get_run_type(self) -> RunType:
        val = random.random()
        if val <= 0.2:
            return RunType.ONE
        elif 0.3 <= val <= 0.5:
            return RunType.TWO
        elif 0.6 <= val <= 0.8:
            return RunType.FOUR
        else:
            return RunType.SIX

    def _is_wicket_taken(self) -> bool:
        # random function return value between 0 and 1
        if random.random() < 0.2:
            return True
        else:
            return False
