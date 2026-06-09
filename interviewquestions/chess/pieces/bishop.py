from .piece import Piece
from ..enums.piece_type import PieceType


class Bishop(Piece):
    def __init__(self, colour):
        super().__init__(colour, PieceType.BISHOP)

    def is_valid_move(self, board, start, end):
        if start == end:
            return False

        if end.get_piece() is not None and end.get_piece().get_colour() == start.get_piece().get_colour():
            return False

        row_diff = abs(end.get_position().get_row() - start.get_position().get_row())
        col_diff = abs(end.get_position().get_col() - start.get_position().get_col())

        if row_diff == col_diff and self._is_path_clear(board, start, end):
            target_piece = board.get_cell(end.get_position()).get_piece()
            return target_piece is None or target_piece.get_colour() != start.get_piece().get_colour()
        return False
