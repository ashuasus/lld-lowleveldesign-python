class Move:
    def __init__(self, player, start, end):
        self._player = player
        self._start = start
        self._end = end
        self._piece_moved = start.get_piece()
        self._piece_killed = None

    def get_player(self):
        return self._player

    def set_player(self, player):
        self._player = player

    def get_start(self):
        return self._start

    def set_start(self, start):
        self._start = start

    def get_end(self):
        return self._end

    def set_end(self, end):
        self._end = end

    def get_piece_moved(self):
        return self._piece_moved

    def set_piece_moved(self, piece_moved):
        self._piece_moved = piece_moved

    def get_piece_killed(self):
        return self._piece_killed

    def set_piece_killed(self, piece_killed):
        self._piece_killed = piece_killed

    def __str__(self):
        return ("Move [player=" + str(self._player) + ", start=" + str(self._start) +
                ", end=" + str(self._end) + ", pieceMoved=" + str(self._piece_moved) +
                ", pieceKilled=" + str(self._piece_killed) + "]")
