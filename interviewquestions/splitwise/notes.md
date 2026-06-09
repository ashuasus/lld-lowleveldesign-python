# Splitwise — Notes

## Design Patterns Used
- **Factory** — `SplitFactory.get_split_object(ExpenseSplitType)` returns the appropriate `ExpenseSplit` validator (`EqualExpenseSplit`, `UnequalExpenseSplit`, `PercentageExpenseSplit`) without the caller knowing the concrete types
- **Strategy** — each `ExpenseSplit` subclass implements `validate_split_request(split_list, total_amount)` differently; swapping split type changes validation behaviour

## Key Classes
- `Splitwise` — top-level facade; owns `UserController`, `GroupController`, and `BalanceSheetController`; the demo method wires them together
- `UserController` — in-memory user registry; provides add/get/get-all operations
- `GroupController` — in-memory group registry; `create_new_group()` adds the creator as the first member
- `Group` — holds members and expense list; `create_expense()` delegates to `ExpenseController`
- `ExpenseController` — validates split via `SplitFactory`, creates `Expense`, and triggers balance sheet update via `BalanceSheetController`
- `BalanceSheetController` — the most complex class; updates `UserExpenseBalanceSheet` for both the payer and each owe-er, and maintains per-user pair `Balance` objects
- `UserExpenseBalanceSheet` — per-user totals: `total_your_expense`, `total_payment`, `total_you_owe`, `total_you_get_back`; plus a `{user_id → Balance}` map for per-pair tracking
- `Balance` — per-user-pair amounts: `amount_owe` (you owe them) and `amount_get_back` (they owe you)
- `Split` — value object: `(user, amount_owe)`; the caller pre-computes amounts
- `ExpenseSplit` — abstract validator base; subclasses validate that the splits add up correctly

## Things to Remember
- **`BalanceSheetController` updates both sides of each split** — for each `Split(user, amount)` in the list: if `user == paid_by`, only `total_your_expense` is incremented (it's your own share). Otherwise, the payer's `total_you_get_back` and per-pair `amount_get_back` are incremented, AND the ower's `total_you_owe` and per-pair `amount_owe` are incremented — two users updated per split.
- **`total_payment` vs `total_your_expense`** — `total_payment` is the full amount paid for the expense; `total_your_expense` is the sum of your own share across all expenses (your actual cost). These are different when you paid for others.
- **Split amounts are pre-computed by the caller** — `Split` is just `(user, amount_owe)`. It's the caller's job to compute the per-person amount. `EqualExpenseSplit.validate_split_request()` only checks that each split's `amount_owe == total / count`; it doesn't compute the split itself.
- **`EqualExpenseSplit` validation is a no-op in effect** — the check `if split.get_amount_owe() != amount_should_be_present: pass` has a `pass` where there should be an exception. Validation silently succeeds even for wrong amounts.
- **Group creates `ExpenseController` in `__init__`** — each `Group` owns its own `ExpenseController` and thereby its own `BalanceSheetController`. There's no shared global balance sheet; balance state is computed fresh per group expense.
- **No debt simplification (minimize transactions)** — the design tracks pairwise balances but does not implement the "simplify debts" feature (find minimum transactions to settle all). This is a common follow-up question in interviews.
- **`user_vs_balance` keyed by `user_id` string** — balance maps use `user_id` (a string like "U1001") as the key, not the `User` object. This allows the dict to be printed easily but requires `user.get_user_id()` calls throughout.
