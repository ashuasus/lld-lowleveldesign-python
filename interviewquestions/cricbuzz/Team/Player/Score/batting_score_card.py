class BattingScoreCard:

    def __init__(self):
        self.total_runs: int = 0
        self.total_balls_played: int = 0
        self.total_fours: int = 0
        self.total_six: int = 0
        self.strike_rate: float = 0.0
        self.wicket_details = None  # Wicket
