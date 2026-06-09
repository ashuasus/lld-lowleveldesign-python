from enum import Enum


class GameStatus(Enum):
    IN_PROGRESS = "IN_PROGRESS"
    BLACK_WIN = "BLACK_WIN"
    WHITE_WIN = "WHITE_WIN"
    DRAW = "DRAW"
    RESIGNATION = "RESIGNATION"
