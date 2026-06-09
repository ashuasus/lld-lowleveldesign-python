# Parking Lot — Notes

## Design Patterns Used
- **Strategy** — `ParkingSpotLookupStrategy` is injected into `ParkingSpotManager`; `RandomLookupStrategy` finds the first free spot (swappable for e.g. closest-to-entrance)
- **Strategy** — `PricingStrategy` is injected into `CostComputation`; `FixedPricingStrategy` always returns 100 (swappable for time-based pricing without touching exit logic)
- **Strategy** — `Payment` is an abstract base with `CashPayment` and `UPIPayment` as concrete strategies, chosen by the caller at exit time
- **Facade** — `ParkingLot` is a thin facade over `ParkingBuilding`, `EntranceGate`, and `ExitGate`; callers only use `vehicle_arrives()` and `vehicle_exits()`

## Key Classes
- `ParkingLot` — top-level facade; wires entrance gate, exit gate, and building together
- `ParkingBuilding` — iterates levels to find the first available level for the vehicle type; creates and returns a `Ticket` on successful allocation
- `ParkingLevel` — holds a `{VehicleType → ParkingSpotManager}` map; routes park/unpark calls to the right manager
- `ParkingSpotManager` — abstract base with spots list, lookup strategy, and a `threading.Lock`; `FourWheelerSpotManager` and `TwoWheelerSpotManager` extend without adding logic
- `RandomLookupStrategy` — scans spot list linearly, returns the first free spot
- `EntranceGate` — stateless; calls `building.allocate(vehicle)` and returns the ticket
- `ExitGate` — computes price via `CostComputation`, processes payment, then calls `building.release(ticket)`
- `CostComputation` — bridges `ExitGate` to the active `PricingStrategy`
- `Ticket` — records vehicle, level, spot, and entry timestamp; the only artefact linking entry to exit

## Things to Remember
- **Per-manager lock, not per-spot** — `threading.Lock` lives in `ParkingSpotManager`, protecting the entire spot list for that vehicle type on that level. Coarser than per-spot locking but sufficient because lookup iterates all spots anyway.
- **`has_free_spot()` also acquires the lock** — prevents a TOCTOU race where two threads both see availability but only one spot remains before either can call `park()`.
- **`Ticket` stores the `ParkingLevel` reference directly** — at exit, `building.release(ticket)` calls `ticket.get_level().un_park(...)`. The ticket is the sole coupling between entry and exit; no look-up table needed.
- **Level-first, not spot-first allocation** — `ParkingBuilding` picks the first level with any availability; there's no attempt to balance load across levels.
- **`RandomLookupStrategy` is misnamed** — despite the name it's a deterministic linear scan, not random. The name signals replaceability of the strategy, not the algorithm.
- **`PricingStrategy.calculate(ticket)`** — receives the full `Ticket` so a future time-based strategy can read `get_entry_time()` without changing the interface.
