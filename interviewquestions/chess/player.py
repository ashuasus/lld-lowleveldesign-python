class Player:
    def __init__(self, name, playing_side):
        self._name = name
        self._playing_side = playing_side

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_playing_side(self):
        return self._playing_side

    def set_playing_side(self, playing_side):
        self._playing_side = playing_side

    def __str__(self):
        return self._name
