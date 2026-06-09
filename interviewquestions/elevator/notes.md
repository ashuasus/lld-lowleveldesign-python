# Elevator System — Notes

## Design Patterns Used
- **Strategy** — `ElevatorSelectionStrategy` is injected into `ElevatorScheduler`; `NearestElevatorStrategy` and `LeastBusyStrategy` are swappable at runtime via `set_strategy()`
- **Singleton** — `InternalDispatcher` uses `__new__` to guarantee a single global instance; the companion `get_instance()` classmethod is a convenience wrapper
- **Template Method (implicit)** — `ElevatorController.run()` calls `_control_elevator()`, which defines the fixed SCAN loop; subclasses could override without changing the threading entry point

## Key Classes
- `ElevatorCar` — physical car state: current floor, direction, door; drives itself floor-by-floor inside `move_elevator()`
- `ElevatorController` — one `threading.Thread` per car; owns two priority queues (`up_min_pq`, `down_max_pq`) and wakes/sleeps via `threading.Condition`
- `ElevatorScheduler` — holds all controllers and delegates car selection to the active strategy
- `ExternalDispatcher` — entry point for hall-button presses; routes to the scheduler to pick a car
- `InternalDispatcher` — Singleton; entry point for in-car button presses; bypasses selection and pushes directly to a specific controller
- `NearestElevatorStrategy` — prefers a car already moving in the same direction toward the caller; falls back to IDLE, then first car
- `LeastBusyStrategy` — picks the car with the fewest queued stops (`len(up_pq) + len(down_pq)`)
- `Floor` — owns up/down `ExternalButton` objects; delegates presses to the dispatcher
- `Building` — creates all floors wired to the shared `ExternalDispatcher`

## Things to Remember
- **SCAN algorithm** — `ElevatorController` uses a min-heap for up-requests and a max-heap (stored as negatives) for down-requests. It fully drains the up-queue in ascending order, then the down-queue in descending order — exactly like a disk head scan. This minimises direction reversals.
- **Two heaps, not one queue** — classifying a new request into up vs down uses a simple heuristic: if `destination >= next_floor_stoppage` it goes to up-heap, else down-heap. This can misclassify when the car is moving down, but it keeps the code simple.
- **Condition variable** — the controller thread sleeps (`_condition.wait()`) when both heaps are empty and wakes on `_condition.notify()` triggered by `_enqueue_request`. The lock is re-acquired around every heap mutation to keep the queues thread-safe.
- **Daemon threads** — both controller threads are set as `daemon=True`, so the process exits cleanly when the main thread finishes without needing explicit `join()` or shutdown signals.
- **Duplicate suppression** — `_enqueue_request` checks membership before pushing (`if destination_floor not in self.up_min_pq`) to avoid serving the same floor twice; note this is O(n) on a list-backed heap.
- **InternalDispatcher vs ExternalDispatcher** — internal buttons know *which* elevator they belong to and skip the scheduler entirely. External (hall) buttons don't know which elevator will come; they go through the scheduler.
- **NearestElevatorStrategy fallback chain** — same-direction candidate → any IDLE car → `controllers[0]`. This ensures a car is always assigned even under heavy load.
