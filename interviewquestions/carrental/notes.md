# Car Rental System — Notes

## Design Patterns Used
- **Strategy** — billing (daily/hourly) and payment (UPI/cash) are interchangeable
- **Facade** — `Store` hides the four managers behind a clean API
- **Repository** — `ReservationRepository` isolates persistence

## Concurrency
- Per-vehicle locks in `VehicleInventoryManager` — threads booking different vehicles never contend
- `setdefault` used for atomic lock creation (avoids check-then-insert race)
- `pop(key, None)` used in `ReservationRepository.remove` (avoids check-then-delete race)
- `reserve()` re-checks availability **inside** the lock to prevent TOCTOU race

## Key Classes
- `VehicleRentalSystem` — top-level, holds stores and users
- `Store` — facade; owns inventory, reservation, billing, payment managers
- `VehicleInventoryManager` — availability checks, thread-safe reserve/release
- `ReservationManager` — lifecycle: SCHEDULED → IN_USE → COMPLETED / CANCELLED
- `DailyBillingStrategy` — bill = (days + 1) × daily_rate

## Things to Remember
- `ReservationRepository` exists to break a circular dependency: `ReservationManager` depends on `VehicleInventoryManager` (to call `reserve/release`), and `VehicleInventoryManager` needs to look up reservations by ID to check date overlaps. If `VehicleInventoryManager` held a reference to `ReservationManager`, you'd have A → B → A. The fix: extract the reservation map (`reservation_id → Reservation`) into a separate `ReservationRepository`. Both `ReservationManager` and `VehicleInventoryManager` depend on it — no cycle.
