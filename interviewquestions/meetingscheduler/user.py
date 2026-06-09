from .calendar import Calendar
from .participant_response import ParticipantResponse


class User:
    def __init__(self, name, email, participant_type):
        self._name = name
        self._email = email
        self._calendar = Calendar()
        self._participant_type = participant_type

    def view_calendar(self):
        print("\n===>>> Displaying " + self._name + "'s calendar for the day:")
        print(self._calendar)

    def respond_to_invitation(self, participant, meeting, response):
        meeting.get_attendees()[participant] = response
        print("[+] " + participant.get_name() + " responded: " + str(response))
        # Update User calendar based on response
        if response == ParticipantResponse.DECLINED:
            self._calendar.remove_meeting(meeting)
        elif response == ParticipantResponse.ACCEPTED:
            self._calendar.add_meeting(meeting)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_calendar(self):
        return self._calendar

    def set_calendar(self, calendar):
        self._calendar = calendar

    def get_participant_type(self):
        return self._participant_type

    def set_participant_type(self, participant_type):
        self._participant_type = participant_type

    def __str__(self):
        return "User [name=" + self._name + ", email=" + self._email + ", participantType=" + str(self._participant_type) + "]"
