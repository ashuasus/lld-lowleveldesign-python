# Snake & Ladder — Notes

## Design Patterns Used
- **Unified Jump abstraction** — no separate Snake and Ladder classes; a single `Jump` object with `start` and `end` fields represents both. `start < end` = ladder (go up), `start > end` = snake (go down). Eliminates a full parallel class hierarchy.

## Key Classes
- `Game` — top-level controller; initialises board, dice, players; runs the game loop until a winner is found
- `Board` — creates a 2D grid of `Cell` objects; randomly assigns snake and ladder `Jump` objects to cells during construction
- `Cell` — holds an optional `Jump` reference; most cells have `jump = None`
- `Jump` — value object with `start` and `end` positions; dual-purpose for snakes and ladders
- `Dice` — supports multiple dice (`dice_count`); `roll_dice()` sums `dice_count` random rolls of 1–6
- `Player` — holds player ID and current position (integer, 0-based)

## Things to Remember
- **`Jump` unifies snakes and ladders** — one class, two roles: `start < end` = ladder, `start > end` = snake. Player always moves to `end`, direction is irrelevant.
- **No zigzag row traversal** — positions are serial (0, 1, 2, ... across every row). Since we only jump between positions, row direction doesn't matter.
