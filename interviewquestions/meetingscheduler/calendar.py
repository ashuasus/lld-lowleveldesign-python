# User has their Calendar for the day
# A meeting room has its Calendar for the day
class Calendar:
    def __init__(self):
        self._meetings = {}

    def add_meeting(self, meeting):
        self._meetings[id(meeting.get_time_interval())] = meeting

    def remove_meeting(self, meeting):
        key = id(meeting.get_time_interval())
        if key in self._meetings:
            del self._meetings[key]

    def get_meeting(self, time_interval):
        return self._meetings.get(id(time_interval))

    def get_meetings(self):
        return list(self._meetings.values())

    def set_meetings(self, meetings):
        self._meetings = meetings

    def __str__(self):
        builder = []
        for m in self._meetings.values():
            builder.append(str(m) + "\n")
        return "".join(builder)
