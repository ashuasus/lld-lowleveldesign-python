from abc import ABC, abstractmethod
from ..enums.piece_colour import PieceColour
from ..enums.piece_type import PieceType


class Piece(ABC):
    def __init__(self, colour, piece_type):
        self._colour = colour
        self._is_captured = False
        self._piece_type = piece_type

    def get_colour(self):
        return self._colour

    def set_colour(self, colour):
        self._colour = colour

    def is_captured(self):
        return self._is_captured

    def set_captured(self, captured):
        self._is_captured = captured

    def get_piece_type(self):
        return self._piece_type

    def set_piece_type(self, piece_type):
        self._piece_type = piece_type

    def _is_path_clear(self, board, start, end):
        from ..position import Position
        end_row = end.get_position().get_row()
        end_col = end.get_position().get_col()
        start_row = start.get_position().get_row()
        start_col = start.get_position().get_col()

        row_diff = end_row - start_row
        col_diff = end_col - start_col
        row_dir = (row_diff > 0) - (row_diff < 0)
        col_dir = (col_diff > 0) - (col_diff < 0)

        current_row = start_row + row_dir
        current_col = start_col + col_dir

        while current_row != end_row or current_col != end_col:
            if board.get_cell(Position(current_row, current_col)).get_piece() is not None:
                return False
            current_row += row_dir
            current_col += col_dir
        return True

    @abstractmethod
    def is_valid_move(self, board, start, end):
        pass

    def __str__(self):
        symbols = {
            PieceType.KING: "K",
            PieceType.QUEEN: "Q",
            PieceType.ROOK: "R",
            PieceType.BISHOP: "B",
            PieceType.KNIGHT: "N",
            PieceType.PAWN: "P",
        }
        symbol = symbols.get(self._piece_type, "?")
        return symbol if self._colour == PieceColour.WHITE else symbol.lower()
