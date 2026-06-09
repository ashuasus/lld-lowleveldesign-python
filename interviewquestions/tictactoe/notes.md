# Tic Tac Toe — Notes

## Design Patterns Used
- **Deque for turn rotation** — `TicTacToeGame` uses `collections.deque` for the players list; `popleft()` on a valid move puts the player at the back via `append()`, and `appendleft()` on an invalid move re-queues the same player at the front so they retry

## Key Classes
- `TicTacToeGame` — owns the board and players deque; `start_game()` runs the main loop; `check_for_winner()` checks all four win conditions after each valid move
- `Board` — NxN grid (default 3); `add_piece()` rejects occupied cells and returns `False`; `get_free_cells()` returns all empty (row, col) tuples; `print_board()` renders the current state
- `Player` — holds name and a `PlayingPiece` reference
- `PlayingPiece` — holds a `PieceType` enum; `PlayingPieceX` and `PlayingPieceO` are the two concrete subclasses
- `GameStatus` — enum: `IN_PROGRESS`, `WIN`, `DRAW`

## Things to Remember
- **`appendleft()` on invalid move** — if a player enters an already-occupied cell, `add_piece()` returns `False`, the player is put back at the front of the deque with `appendleft()`, and the loop continues. No turn is consumed. This is the key deque trick — normal circular rotation uses `popleft` + `append`; retry uses `popleft` + `appendleft`.
- **`check_for_winner()` only checks the row/column/diagonals of the last move** — it takes `(row, column, piece_type)` as arguments and checks only the row that `row` is in, the column that `column` is in, and both diagonals. It doesn't scan the whole board. This is O(n) not O(n²).
- **Draw detection** — after a valid move fails to win, the loop calls `get_free_cells()` at the start of the next iteration. If the list is empty, `no_winner = False` ends the loop and `start_game()` returns `GameStatus.DRAW`.
- **`Board` is parameterised by size** — `Board(3)` for standard Tic Tac Toe, but it could be `Board(5)` for a larger variant. `check_for_winner()` uses `self.game_board.size` for all loop bounds, so it scales correctly.
- **`PlayingPieceX` and `PlayingPieceO` are distinct classes** — they exist purely to make piece identity clear; both inherit from `PlayingPiece` and pass `PieceType.X` or `PieceType.O` to the constructor. In practice a single `PlayingPiece(PieceType.X)` would work the same, but separate classes make instantiation more expressive.
- **No AI or computer player** — the game reads from `input()`, so it requires a human at both sides. A common extension is to add a `ComputerPlayer` with a strategy (random, minimax).
- **Win check does not short-circuit early** — all four checks (row, column, diagonal, anti-diagonal) are computed as booleans before the final `return row_match or column_match or ...`. Python's `or` short-circuits at evaluation time, so in practice it does stop early, but the loop structure runs all four checks anyway.
