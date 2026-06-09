class TimeInterval:
    def __init__(self, start_time, end_time):
        self._start_time = start_time
        self._end_time = end_time

    def get_start_time(self):
        return self._start_time

    def get_end_time(self):
        return self._end_time

    def overlaps_with(self, new_interval):
        # if the current interval ends before the new interval starts - valid: overlaps? false
        # if the current interval starts after the new interval ends - valid: overlaps? false
        return not (self._end_time < new_interval._start_time) and not (self._start_time > new_interval._end_time)
