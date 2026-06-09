# ATM — Notes

## Design Patterns Used
- **State** — `ATM` holds a `current_atm_state` reference; each state class (`IdleState`, `HasCardState`, `SelectOperationState`, `CashWithdrawalState`, `CheckBalanceState`) implements the same interface and transitions the ATM to the next state
- **Chain of Responsibility** — cash dispensing is handled by a linked chain: `TwoThousandWithdrawProcessor → FiveHundredWithdrawProcessor → OneHundredWithdrawProcessor`; each processor handles as many of its denomination as available and forwards the remainder to the next node
- **Singleton** — `ATM` uses `__new__` to ensure only one ATM object ever exists

## Key Classes
- `ATM` — Singleton; holds note counts (2000/500/100), total balance, and the active `ATMState`
- `ATMRoom` — bootstraps the system: creates the ATM, sets balance/notes, creates user and card
- `ATMState` — base class with all operations as no-ops (print error); subclasses override only the operations valid in that state
- `IdleState` — only `insert_card()` is meaningful; transitions to `HasCardState`
- `HasCardState` — only `authenticate_pin()` is meaningful; transitions to `SelectOperationState` on correct PIN or ejects card on wrong PIN
- `SelectOperationState` — only `select_operation()` is meaningful; branches to `CashWithdrawalState` or `CheckBalanceState`
- `CashWithdrawalState` — validates ATM balance and bank balance, deducts both, triggers the withdrawal chain, then ejects card and returns to `IdleState`
- `CheckBalanceState` — prints bank balance, ejects card, returns to `IdleState`
- `CashWithdrawProcessor` — abstract node in the Chain of Responsibility; holds a reference to the next processor
- `TwoThousandWithdrawProcessor` / `FiveHundredWithdrawProcessor` / `OneHundredWithdrawProcessor` — concrete handlers that dispense as many notes of their denomination as available

## Things to Remember
- **State base class as default error handler** — `ATMState` defines every operation to print "OOPS!! Something went wrong". Subclasses only override valid operations. This means calling `authenticate_pin()` on `IdleState` automatically fails without any explicit guard — a clean way to enforce state-machine invariants.
- **Deferred imports to break circular dependencies** — each state class does `from .has_card_state import HasCardState` (etc.) inside the method body, not at the top. This is because all state files import from each other in a cycle; top-level imports would cause `ImportError`.
- **Chain of Responsibility handles partial denominations** — if the ATM has fewer notes than required (e.g. only 1 × ₹2000 note but ₹3000 requested), the processor deducts what it has and passes the remaining ₹1000 downstream. The final `OneHundredWithdrawProcessor` prints an error if it can't cover the remainder — but note: balance was already deducted before building the chain, so a shortage at dispensing is a design bug.
- **Two balance checks before dispensing** — `CashWithdrawalState` checks both `atm.get_atm_balance()` (notes in machine) and `card.get_bank_balance()` (user's account). Both are checked before any deduction.
- **`ATM.get_atm_object()`** — the canonical factory method: calls `ATM()` (which is `__new__`-controlled) then calls `set_current_atm_state(IdleState())` to ensure every Singleton access starts in Idle.
- **Chain is built fresh per withdrawal** — the processor chain is constructed inside `CashWithdrawalState.cash_withdrawal()` on every call. There's no shared chain instance; each transaction gets its own chain object.
