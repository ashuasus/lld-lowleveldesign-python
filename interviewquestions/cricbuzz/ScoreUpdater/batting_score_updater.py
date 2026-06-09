from .score_updater_observer import ScoreUpdaterObserver
from ..Inning.run_type import RunType


class BattingScoreUpdater(ScoreUpdaterObserver):

    def update(self, ball_details) -> None:
        run = 0

        if RunType.ONE == ball_details.run_type:
            run = 1
        elif RunType.TWO == ball_details.run_type:
            run = 2
        elif RunType.FOUR == ball_details.run_type:
            run = 4
            ball_details.played_by.batting_score_card.total_fours += 1
        elif RunType.SIX == ball_details.run_type:
            run = 6
            ball_details.played_by.batting_score_card.total_six += 1

        ball_details.played_by.batting_score_card.total_runs += run
        ball_details.played_by.batting_score_card.total_balls_played += 1

        if ball_details.wicket is not None:
            ball_details.played_by.batting_score_card.wicket_details = ball_details.wicket
