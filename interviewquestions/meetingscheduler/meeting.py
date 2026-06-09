from .participant_response import ParticipantResponse


class Meeting:
    def __init__(self, meeting_id, subject, time_interval, organizer, attendees, meeting_room):
        self._meeting_id = meeting_id
        self._subject = subject
        self._time_interval = time_interval
        self._organizer = organizer
        self._meeting_room = meeting_room
        self._attendees = attendees

    def get_meeting_id(self):
        return self._meeting_id

    def set_meeting_id(self, meeting_id):
        self._meeting_id = meeting_id

    def get_subject(self):
        return self._subject

    def set_subject(self, subject):
        self._subject = subject

    def get_time_interval(self):
        return self._time_interval

    def set_time_interval(self, time_interval):
        self._time_interval = time_interval

    def get_organizer(self):
        return self._organizer

    def set_organizer(self, organizer):
        self._organizer = organizer

    def get_meeting_room(self):
        return self._meeting_room

    def set_meeting_room(self, meeting_room):
        self._meeting_room = meeting_room

    def get_attendees(self):
        return self._attendees

    def set_attendees(self, attendees):
        self._attendees = attendees

    def get_accepted_participants(self):
        return [user for user, response in self._attendees.items() if response == ParticipantResponse.ACCEPTED]

    def get_declined_participants(self):
        return [user for user, response in self._attendees.items() if response == ParticipantResponse.DECLINED]

    def get_tentative_participants(self):
        return [user for user, response in self._attendees.items() if response == ParticipantResponse.TENTATIVE]

    def __str__(self):
        return ("Meeting [meetingId=" + self._meeting_id + ", subject=" + self._subject +
                ", organizer=" + self._organizer.get_name() + ", meetingRoom=" + self._meeting_room.get_name() + "]")
