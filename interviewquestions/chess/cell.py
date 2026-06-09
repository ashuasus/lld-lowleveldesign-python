class Cell:
    def __init__(self, piece, position):
        self._piece = piece
        self._position = position

    def get_piece(self):
        return self._piece

    def set_piece(self, piece):
        self._piece = piece

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def __str__(self):
        return "Cell [piece=" + str(self._piece) + ", position=" + str(self._position) + "]"
