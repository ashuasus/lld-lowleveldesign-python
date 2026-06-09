class Position:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    def get_row(self):
        return self._row

    def get_col(self):
        return self._col

    def is_valid(self):
        return 0 <= self._row < 8 and 0 <= self._col < 8

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self._row == other._row and self._col == other._col

    def __hash__(self):
        return hash((self._row, self._col))

    def __str__(self):
        return chr(ord('a') + self._col) + str(self._row + 1)
