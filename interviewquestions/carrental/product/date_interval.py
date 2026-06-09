class DateInterval:
    def __init__(self, from_date, to_date):
        if to_date < from_date:
            raise ValueError("End date cannot be before start date")
        self._from = from_date
        self._to = to_date

    def get_from(self):
        return self._from

    def get_to(self):
        return self._to

    def overlaps(self, other):
        return not (self._to < other._from or self._from > other._to)
