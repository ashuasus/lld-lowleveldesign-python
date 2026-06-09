import time
from .meeting import Meeting
from .notification import Notification
from .participant_response import ParticipantResponse


class MeetingScheduler:
    def __init__(self, rooms):
        self._all_meeting_rooms = rooms

    def schedule_meeting(self, organiser, participants, subject, time_interval):
        # Check for available meeting rooms with available time slots
        room = self._check_for_available_rooms(len(participants), time_interval)
        if room is None:
            print("===>>> No available meeting room")
            return None
        print("\n===>>> Available meeting room found")
        # Create meeting
        meeting = Meeting(self._get_meeting_id(), subject, time_interval, organiser, participants, room)

        # Add meeting to participants(both organiser and participants) calendar
        organiser.get_calendar().add_meeting(meeting)
        for user in participants.keys():
            user.get_calendar().add_meeting(meeting)
        # Add meeting to meeting room calendar
        self._book_slot(room, meeting)

        # Notify participants
        self._notify_participants_with_invites(meeting)
        self._simulate_user_responses_for_invites(meeting)
        print("[+] Meeting scheduled successfully!!")

        return meeting

    def cancel_meeting(self, meeting):
        print("\n===>>> Cancelling meeting: " + meeting.get_meeting_id() + " - " + meeting.get_subject())
        self._release_slot(meeting.get_meeting_room(), meeting)

        # Notify participants
        self._notify_participants_about_meeting_cancellation(meeting)

    def _simulate_user_responses_for_invites(self, meeting):
        for user in meeting.get_attendees().keys():
            user.respond_to_invitation(user, meeting, ParticipantResponse.ACCEPTED)

    def _get_meeting_id(self):
        str_val = str(int(time.time() * 1000))
        return "MTS-" + str_val[-4:]

    def add_meeting_room(self, meeting_room):
        self._all_meeting_rooms.append(meeting_room)

    def remove_meeting_room(self, meeting_room):
        self._all_meeting_rooms.remove(meeting_room)

    def _notify_participants_with_invites(self, meeting):
        notification = Notification(1, "Meeting Invitation: " + meeting.get_subject())
        meeting.get_organizer().get_calendar().add_meeting(meeting)
        for user in meeting.get_attendees().keys():
            user.get_calendar().add_meeting(meeting)
            notification.send_meeting_invite_notification(user, meeting)

    def _notify_participants_about_meeting_cancellation(self, meeting):
        notification = Notification(2, "Meeting Cancelled: " + meeting.get_meeting_id() + " - " + meeting.get_subject())
        meeting.get_organizer().get_calendar().remove_meeting(meeting)
        for user in meeting.get_accepted_participants():
            user.get_calendar().remove_meeting(meeting)
            notification.send_cancel_meeting_notification(user, meeting)

    def _book_slot(self, room, meeting):
        room.add_booked_slot(meeting.get_time_interval())
        room.get_calendar().add_meeting(meeting)

    def _release_slot(self, room, meeting):
        room.remove_booked_slot(meeting.get_time_interval())
        room.get_calendar().remove_meeting(meeting)

    def _check_for_available_rooms(self, capacity, interval):
        for room in self._all_meeting_rooms:
            if room.is_available_for(interval, capacity):
                return room
        return None
