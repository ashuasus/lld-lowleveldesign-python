from .piece import Piece
from ..enums.piece_type import PieceType
from ..enums.piece_colour import PieceColour


class Pawn(Piece):
    def __init__(self, colour):
        super().__init__(colour, PieceType.PAWN)

    def is_valid_move(self, board, start, end):
        if start == end:
            return False

        if end.get_piece() is not None and end.get_piece().get_colour() == start.get_piece().get_colour():
            return False

        direction = 1 if self.get_colour() == PieceColour.WHITE else -1

        row_diff = abs(end.get_position().get_row() - start.get_position().get_row())
        col_diff = abs(end.get_position().get_col() - start.get_position().get_col())

        # Move forward - 1 step
        if col_diff == 0 and row_diff == 1:
            return board.get_cell(end.get_position()).get_piece() is None

        # First move - 2 steps
        if col_diff == 0 and not self._has_moved_before(start) and row_diff == 2:
            from ..position import Position
            intermediate = Position(start.get_position().get_row() + direction, start.get_position().get_col())
            return (board.get_cell(intermediate).get_piece() is None and
                    board.get_cell(end.get_position()).get_piece() is None)

        # Capture - diagonal
        if col_diff == 1 and row_diff == 1:
            target_piece = board.get_cell(end.get_position()).get_piece()
            return target_piece is not None and target_piece.get_colour() != start.get_piece().get_colour()
        return False

    def _has_moved_before(self, start):
        return start.get_position().get_row() != 1 and start.get_position().get_row() != 6
