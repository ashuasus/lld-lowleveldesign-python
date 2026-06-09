# Payment Gateway — Notes

## Design Patterns Used
- **Factory** — `InstrumentServiceFactory.get_instrument_service(InstrumentType)` returns a `BankService` or `CardService` based on the instrument type; callers (including `InstrumentController`) never instantiate services directly
- **Data Object (DO) pattern** — `InstrumentDO`, `TransactionDO`, `UserDO` are flat data containers passed across layer boundaries; internal domain objects (`BankInstrument`, `CardInstrument`, `User`, `Transaction`) stay within the service layer and are never exposed
- **Layered Architecture (Controller → Service)** — `UserController`, `InstrumentController`, `TransactionController` are thin delegators; all logic lives in `UserService`, `BankService`/`CardService`, `TransactionService`

## Key Classes
- `PaymentGateway` (the demo/main) — assembles controllers, registers users and instruments, makes a payment, and queries history
- `InstrumentController` — delegates add/fetch to `InstrumentServiceFactory`; `get_all_instruments()` fetches from both `BankService` and `CardService` and merges the results
- `InstrumentServiceFactory` — Factory; maps `InstrumentType → InstrumentService` implementation
- `InstrumentService` — abstract base with a **class-level** `user_vs_instruments` dict shared across all subclass instances (acts as an in-memory store)
- `BankService` / `CardService` — concrete services; persist `BankInstrument`/`CardInstrument` objects in the shared `user_vs_instruments` dict and return `InstrumentDO` (not domain objects)
- `TransactionService` — resolves sender/receiver instruments via `InstrumentController`, calls `Processor.process_payment()`, records the transaction in a **class-level** `user_vs_transactions_list` dict for both sender and receiver
- `Processor` — stub for actual payment network integration; currently a no-op placeholder
- `UserService` — creates `User` domain objects, assigns random IDs, persists in a **class-level** `users_list`
- `InstrumentDO` / `TransactionDO` / `UserDO` — transfer objects carrying flat fields across layer boundaries

## Things to Remember
- **Class-level dicts as in-memory databases** — `InstrumentService.user_vs_instruments`, `TransactionService.user_vs_transactions_list`, and `UserService.users_list` are all class variables. Every instance of `BankService` and `CardService` shares the same `user_vs_instruments` dict. This is intentional (simulates a shared data store) but is surprising in Python where class variables are mutable and shared by reference.
- **DO pattern separates domain from API** — `BankService.add_instrument()` stores a `BankInstrument` domain object but returns an `InstrumentDO`. Controllers never hold domain objects; they work only with DOs. This is a Java-style DAO pattern.
- **`InstrumentController.get_all_instruments()` fetches both types** — it creates a `BankService` AND a `CardService` instance and merges their results. Since `user_vs_instruments` is a class variable, both services read from the same dict but each filters by its own `InstrumentType`.
- **`BankService` and `CardService` filter by `InstrumentType` in `get_instruments_by_user_id()`** — all instruments for a user (both bank and card) are stored in one list in `user_vs_instruments`. Each service retrieves the list and filters by type. This means if you call `BankService().get_instruments_by_user_id()` you only get bank instruments, even though the dict holds both.
- **`Processor` is a deliberate stub** — `process_payment()` has commented pseudo-code for validate → process → debit → credit but no implementation. The transaction is hardcoded to `SUCCESS` in `TransactionService`. In an interview, describe this as "the network call to the acquiring bank."
- **Random IDs** — both `UserService` and `BankService`/`CardService` use `random.randint(10, 99)` for IDs. Collision probability is high in demos with many users/instruments; this is acceptable for illustration but would need a UUID or DB sequence in production.
- **Transaction is stored for BOTH sender and receiver** — `TransactionService.make_payment()` appends the same `Transaction` object to both `sender_txns_list` and `receiver_txn_list`. So both users can query their transaction history and see this transfer.
