# Chess — Notes

## Design Patterns Used
- **Template Method** — `Piece` defines the abstract `is_valid_move()` that each concrete piece must implement; `Piece` also provides `_is_path_clear()` as a shared helper used by Rook, Bishop, and Queen
- **Polymorphism** — `Game._make_move()` calls `start_piece.is_valid_move(board, start, end)` without knowing the concrete piece type; each piece enforces its own movement rules

## Key Classes
- `Game` — owns `Board`, two `Player` objects, move history, and current turn tracking; `_make_move()` is the core: validates ownership, calls piece logic, executes the move, detects checkmate
- `Board` — 8×8 grid of `Cell` objects; initialises standard piece placement; `get_cell(Position)` bounds-checks and exits on invalid access
- `Cell` — holds an optional `Piece` and a `Position`; the mutable unit of the board
- `Position` — value object (row, col); implements `__eq__` and `__hash__` for use as dict keys; `__str__` renders algebraic notation (e.g. `e4`)
- `Move` — records player, start cell, end cell, piece moved, and piece killed; appended to `_moves_history` after each turn
- `Piece` — abstract base with colour, captured flag, and `_is_path_clear()` shared path-checking logic
- `Pawn` — the most complex piece: forward-only movement with direction derived from colour; two-square first move checks initial row (row 1 or 6); diagonal capture requires an enemy piece to be present
- `Knight` — only piece that ignores `_is_path_clear()`; L-shaped move check is just `(2,1) or (1,2)` absolute differences
- `King` — one-square move in any direction; no castling implemented
- `Queen` — union of Rook and Bishop rules: straight or diagonal with path-clear check
- `Player` — holds name and playing side (WHITE/BLACK)

## Things to Remember
- **Checkmate detection is capture-based** — `_make_move()` checks `isinstance(end_piece, King)` after the move executes. The game ends when the King is physically captured, not when it is in check. This is a simplification: real chess ends on checkmate (check with no escape), not on King capture.
- **`_is_path_clear()` uses sign arithmetic** — it computes `row_dir` and `col_dir` as -1/0/+1 by comparing difference sign, then steps from start to end (exclusive), checking each intermediate cell. Knight skips this because it jumps.
- **Pawn direction from colour** — `direction = 1 if WHITE else -1`. White pawns at row 1 move toward row 7; black at row 6 move toward row 0. The initial two-square move checks `not self._has_moved_before(start)`, which tests whether the pawn is still on its starting row (1 for white, 6 for black).
- **Board initialises pieces directly** — `Board._init_pieces()` hard-codes standard chess setup with `cells[0]` as white back rank and `cells[7]` as black back rank. Row 0 = White, Row 7 = Black.
- **`get_cell()` calls `sys.exit(0)` on out-of-bounds** — rather than raising an exception, an invalid position terminates the program. In an interview this is acceptable but worth noting as a design smell.
- **Move history for replay** — `_moves_history` is a list of `Move` objects. `display_moves_history()` prints them. This is the hook for undo/redo but undo is not implemented.
- **Turn toggle is unconditional** — even if a move fails (returns `False`), the turn does NOT toggle; the `if self._current_turn == self._player1` toggle happens only on the success path inside `_make_move()`.
- **No en passant, promotion, or castling** — purely illustrative; mention these omissions in an interview.
