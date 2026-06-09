from .score_updater_observer import ScoreUpdaterObserver
from ..Inning.ball_type import BallType
from ..Inning.run_type import RunType


class BowlingScoreUpdater(ScoreUpdaterObserver):

    def update(self, ball_details) -> None:
        if ball_details.ball_number == 6 and ball_details.ball_type == BallType.NORMAL:
            ball_details.bowled_by.bowling_score_card.total_overs_count += 1

        if RunType.ONE == ball_details.run_type:
            ball_details.bowled_by.bowling_score_card.runs_given += 1
        elif RunType.TWO == ball_details.run_type:
            ball_details.bowled_by.bowling_score_card.runs_given += 2
        elif RunType.FOUR == ball_details.run_type:
            ball_details.bowled_by.bowling_score_card.runs_given += 4
        elif RunType.SIX == ball_details.run_type:
            ball_details.bowled_by.bowling_score_card.runs_given += 6

        if ball_details.wicket is not None:
            ball_details.bowled_by.bowling_score_card.wickets_taken += 1

        if ball_details.ball_type == BallType.NOBALL:
            ball_details.bowled_by.bowling_score_card.no_ball_count += 1

        if ball_details.ball_type == BallType.WIDEBALL:
            ball_details.bowled_by.bowling_score_card.wide_ball_count += 1
