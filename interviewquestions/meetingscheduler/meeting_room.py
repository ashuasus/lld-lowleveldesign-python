from .calendar import Calendar


class MeetingRoom:
    def __init__(self, room_id, name, capacity):
        self._id = room_id
        self._name = name
        self._capacity = capacity
        self._booked_slots = []
        self._calendar = Calendar()

    def view_calendar(self):
        print("\n===>>> Displaying Meeting " + self._name + "'s calendar for the day:")
        print(self._calendar)

    def get_id(self):
        return self._id

    def get_capacity(self):
        return self._capacity

    def get_calendar(self):
        return self._calendar

    def set_calendar(self, calendar):
        self._calendar = calendar

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_booked_slots(self):
        return self._booked_slots

    def add_booked_slot(self, booked_slot):
        self._booked_slots.append(booked_slot)

    def remove_booked_slot(self, booked_slot):
        self._booked_slots.remove(booked_slot)

    def is_available_for(self, interval, required_capacity):
        if required_capacity > self._capacity:
            return False
        for time_interval in self._booked_slots:
            if time_interval.overlaps_with(interval):
                return False
        return True
