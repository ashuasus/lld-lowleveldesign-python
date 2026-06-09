# Cricbuzz — Notes

## Design Patterns Used
- **Observer** — `BallDetails` holds a list of `ScoreUpdaterObserver` instances (`BattingScoreUpdater`, `BowlingScoreUpdater`); after every ball delivery, it calls `_notify_updaters(self)` to push the `BallDetails` to all observers who update their respective scorecards
- **Template Method** — `MatchType` is an abstract class defining `no_of_overs()` and `max_over_count_bowlers()`; `T20Match` and `OneDayMatch` provide concrete values without changing the innings loop in `InningDetails.start()`
- **Strategy (implicit)** — `Match` and `InningDetails` accept a `MatchType` object; swapping `T20Match` for `OneDayMatch` changes the entire match structure with no other code changes

## Key Classes
- `Match` — orchestrates the full match: toss, two innings, winner determination, scorecard printing
- `InningDetails` — runs one inning: iterates overs, assigns bowlers, breaks early if target is chased; swaps striker/non-striker after each over
- `OverDetails` — runs one over: loops 6 legal balls; handles extra balls without incrementing the counter; breaks early on successful chase
- `BallDetails` — the core event: randomly determines wicket or runs, updates striker/non-striker swap for odd runs, notifies all score updater observers
- `BattingScoreUpdater` — observer that updates the batting player's `BattingScoreCard` (runs, balls, fours, sixes, wicket)
- `BowlingScoreUpdater` — observer that updates the bowling player's `BowlingScoreCard` (overs, runs given, wickets, no-balls, wide-balls)
- `Team` — owns `PlayerBattingController` and `PlayerBowlingController`; delegates striker/non-striker management and bowler selection to them
- `PlayerBattingController` — manages batting order via a `deque`; `get_next_player()` pops the next batter when striker is None
- `PlayerBowlingController` — rotates bowlers via a `deque`; tracks over count per bowler; removes a bowler from rotation when they hit `max_over_count_per_bowler`
- `PlayerDetails` — holds a player's `BattingScoreCard` and `BowlingScoreCard` alongside their personal info
- `MatchType` — abstract base encoding match-specific rules (overs per inning, max overs per bowler)

## Things to Remember
- **Observer on `BallDetails`, not on `InningDetails`** — observers are attached at the finest grain (per ball), not per over or per inning. This allows granular scorecard updates after each delivery, matching real-time scoreboard behaviour.
- **`BowlingScoreUpdater` counts overs at ball 6** — it increments `total_overs_count` only when `ball_details.ball_number == 6 and ball_type == NORMAL`. Extra balls reset the `ball_count` without triggering this, so over count is accurate.
- **Striker/non-striker swap for odd runs** — `BallDetails.start_ball_delivery()` swaps the two batsmen when `RunType.ONE` or `RunType.THREE` is scored. This happens inside `BallDetails`, not in the team or inning — tight coupling to run logic.
- **Deque used for both batting order and bowling rotation** — `PlayerBattingController` uses `deque` as a queue (popleft when a batter falls). `PlayerBowlingController` uses `deque` as a circular queue (popleft then append back unless at over limit).
- **`PlayerBowlingController` keeps a bowler even when at max overs** — `get_next_bowler()` sets `self.current_bowler = player_details` in both the quota-reached and not-reached branches, but only appends back to the deque if quota is not reached. So the last over counts. The logic inside the two branches is identical except for the append — this is a subtle implementation detail.
- **Target chase detection** — `OverDetails.start_over()` checks `batting_team.get_total_runs() >= runs_to_win` after every ball. `runs_to_win` is `-1` in the first inning (never triggers), and set to `innings[0].get_total_runs()` for the second inning.
- **`Match.start_match()` hardcodes toss-winner bats first** — the comment says "assuming here that tossWinner batFirst"; the bowling team is determined by checking team names to avoid the same team batting twice.
- **Run type is random** — `BallDetails._get_run_type()` uses `random.random()` with fixed probability thresholds: ≤0.2 → ONE, 0.3–0.5 → TWO, 0.6–0.8 → FOUR, else SIX. The gap 0.2–0.3 and >0.8 both map to SIX (no zero-run case without wicket).
