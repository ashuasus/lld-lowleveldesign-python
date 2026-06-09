# BookMyShow — Notes

## Design Patterns Used
- **Layered Architecture (Controller → Service → Entity)** — `TheatreController` and `BookingController` are thin delegators to `TheatreService` and `BookingService`; all logic lives in the service layer
- **Two-Phase Locking** — `Show.lock_seats()` acquires per-seat locks in sorted order, validates availability, marks seats `LOCKED`, then releases — preventing deadlock and double-booking simultaneously

## Key Classes
- `BookMyShowApp` — demo driver; creates the full object graph (movies, theatres, screens, shows, seats) and runs a user flow
- `TheatreController` / `TheatreService` — manages theatre registration and discovery: get movies by city/date, get theatres by city/movie/date, get shows
- `BookingController` / `BookingService` — orchestrates the booking flow: lock seats → process payment → confirm or release
- `Theatre` — holds a name, city, and list of `Screen` objects
- `Screen` — holds a list of `Seat` objects and a `{date → [Show]}` map
- `Show` — the central concurrency object; owns a `{seat_id → SeatStatus}` map and a `{seat_id → Lock}` map; exposes `lock_seats()`, `confirm_seats()`, `release_seats()`
- `Seat` — simple value object: seat ID and category (SILVER/GOLD/PLATINUM)
- `Booking` — immutable record of a confirmed booking; stores user, show, seats list, payment, and a UUID booking ID
- `Payment` — value object holding a payment ID and status; created inline with hardcoded SUCCESS in the demo

# Things to Remember

## Why Per-Seat Locks, Not a Show-Level Lock
- A single lock on the whole `Show` forces users booking *different* seats to wait for each other — kills concurrency
- Per-seat locks give higher concurrency but introduce deadlock risk: U1 wants [S1, S5], U2 wants [S5, S1] → U1 holds S1 waiting for S5, U2 holds S5 waiting for S1 → deadlock
- **Fix: sort seat IDs before acquiring locks.** U1 and U2 both acquire in order [S1, S5], so one always waits behind the other instead of deadlocking

## No Separate Controllers for Seats, Screens, or Shows
- There is no `SeatController`, `ScreenController`, or `ShowController` — these entities are tightly coupled and owned by their parents
- `Seat` and `Show` are managed directly by `Screen`; `Screen` is managed directly by `Theatre`
- Only `Theatre` and `Booking` have their own controllers because they represent the two top-level entry points: discovery (find a show) and transactions (book a show)
