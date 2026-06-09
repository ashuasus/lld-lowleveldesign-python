# Meeting Scheduler — Notes

## Design Patterns Used
- **Observer (implicit)** — `MeetingScheduler._notify_participants_with_invites()` and `_notify_participants_about_meeting_cancellation()` push `Notification` objects to each participant; while not a formal Observer registry, the pattern intent is clear
- **Shared Calendar model** — both `User` and `MeetingRoom` own a `Calendar` instance; the scheduler writes to all three on booking and removes from all three on cancellation, keeping everyone's view consistent

## Key Classes
- `MeetingScheduler` — orchestrates scheduling: find a room, create a meeting, update all calendars, notify participants; also handles cancellation
- `MeetingRoom` — holds capacity, a `Calendar`, and a list of booked `TimeInterval` objects; `is_available_for()` checks capacity and interval overlap
- `Meeting` — aggregates all booking data: ID, subject, time interval, organiser, attendees dict (user → response), room; exposes filtered participant lists by response status
- `TimeInterval` — value object with start/end; `overlaps_with()` uses the standard non-overlap negation: `not (end < other.start) and not (start > other.end)`
- `Calendar` — keyed by `id(time_interval)` (Python object identity), not by value; supports `add_meeting()`, `remove_meeting()`, and `get_meetings()`
- `User` — holds name, email, participant type, and a personal `Calendar`; `respond_to_invitation()` updates the attendees dict and syncs the user's calendar based on the response
- `Notification` — simple helper with `send_meeting_invite_notification()` and `send_cancel_meeting_notification()`

## Things to Remember
- **`Calendar` keys by `id(time_interval)`, not value** — `add_meeting()` uses `id(meeting.get_time_interval())` as the dict key. Two `TimeInterval` objects with identical start/end would be treated as different entries. This is fine as long as the same `TimeInterval` instance is used throughout a meeting's lifecycle (which it is, since `Meeting` stores the reference).
- **Attendees dict is `{User → ParticipantResponse}`** — rather than a list of users, attendees is a mutable dict. This allows `User.respond_to_invitation()` to update the response in place: `meeting.get_attendees()[participant] = response`. Accepted participants are filtered with a list comprehension in `get_accepted_participants()`.
- **Room availability checks both capacity and time** — `is_available_for(interval, capacity)` rejects if `capacity > self._capacity` before checking time conflicts. The room is searched first-fit; no optimization for smallest fitting room.
- **`overlaps_with` uses De Morgan's negation** — intervals overlap if it's NOT the case that one ends before the other starts. The code is: `not (end_time < new.start) and not (start_time > new.end)`. Mentally: "two intervals overlap unless one is completely before or after the other."
- **`_notify_participants_with_invites` re-adds meetings to organiser's calendar** — the method is called after `organiser.get_calendar().add_meeting(meeting)` in `schedule_meeting()`, so the meeting is added twice to the organiser's calendar. This is a minor bug in the implementation.
- **Meeting ID is timestamp-based** — `_get_meeting_id()` uses `"MTS-" + str(int(time.time() * 1000))[-4:]`; this takes the last 4 digits of the millisecond timestamp. Collision risk is low for demos but not production-safe.
- **`cancel_meeting` only removes from accepted participants' calendars** — `_notify_participants_about_meeting_cancellation()` iterates `get_accepted_participants()`, not all attendees. Users who DECLINED or haven't responded don't get cancellation notifications (which is correct behaviour).
