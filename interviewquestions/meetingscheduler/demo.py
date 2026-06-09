from datetime import datetime
from .meeting_room import MeetingRoom
from .user import User
from .participant_type import ParticipantType
from .participant_response import ParticipantResponse
from .meeting_scheduler import MeetingScheduler
from .time_interval import TimeInterval


def main():
    print("\n###### LLD Code - Meeting Scheduler Demo ######")

    # Create Rooms
    room1 = MeetingRoom(1, "Room 1", 4)
    room2 = MeetingRoom(2, "Room 2", 8)
    room3 = MeetingRoom(3, "Room 3", 12)
    rooms = [room1, room2, room3]

    # Create Users
    user1 = User("User 1", "user1@example.com", ParticipantType.ORGANIZER)
    participants_m1 = {}
    user2 = User("User 2", "user2@example.com", ParticipantType.ATTENDEE)
    user3 = User("User 3", "user3@example.com", ParticipantType.ATTENDEE)
    user4 = User("User 4", "user4@example.com", ParticipantType.ATTENDEE)
    user5 = User("User 5", "user5@example.com", ParticipantType.ATTENDEE)
    user6 = User("User 6", "user6@example.com", ParticipantType.ATTENDEE)
    user7 = User("User 7", "user7@example.com", ParticipantType.ATTENDEE)
    participants_m1[user2] = ParticipantResponse.NOT_RESPONDED
    participants_m1[user3] = ParticipantResponse.NOT_RESPONDED

    # Create Meeting Scheduler
    meeting_scheduler = MeetingScheduler(rooms)

    # Schedule Meeting
    start_time = datetime(2022, 1, 22, 10, 0)
    end_time = datetime(2022, 1, 22, 11, 0)
    meeting1 = meeting_scheduler.schedule_meeting(user1, participants_m1, "Meeting 1-Requirement Planning", TimeInterval(start_time, end_time))

    participants_m2 = {}
    participants_m2[user4] = ParticipantResponse.NOT_RESPONDED
    participants_m2[user5] = ParticipantResponse.NOT_RESPONDED
    participants_m2[user6] = ParticipantResponse.NOT_RESPONDED
    participants_m2[user7] = ParticipantResponse.NOT_RESPONDED

    meeting2 = meeting_scheduler.schedule_meeting(user3, participants_m2, "Meeting 2-Effort Planning", TimeInterval(start_time, end_time))

    # User's Calendar
    user1.view_calendar()
    user3.view_calendar()

    # Meeting Room's Calendar
    meeting1.get_meeting_room().view_calendar()
    meeting2.get_meeting_room().view_calendar()

    # Cancel Meeting
    meeting_scheduler.cancel_meeting(meeting1)
    meeting_scheduler.cancel_meeting(meeting2)

    # User's Calendar - empty
    user1.view_calendar()
    user3.view_calendar()

    # Meeting Room's Calendar - empty
    meeting1.get_meeting_room().view_calendar()
    meeting2.get_meeting_room().view_calendar()


if __name__ == "__main__":
    main()
