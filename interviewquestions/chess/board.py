from .cell import Cell
from .position import Position
from .enums.piece_colour import PieceColour
from .pieces.rook import Rook
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.queen import Queen
from .pieces.king import King
from .pieces.pawn import Pawn


class Board:
    def __init__(self):
        self.cells = [[None] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8):
                self.cells[i][j] = Cell(None, Position(i, j))
        self._init_pieces()

    def get_cell(self, position):
        i = position.get_row()
        j = position.get_col()
        if i < 0 or i > 7 or j < 0 or j > 7:
            print("[ERR] Index out of bound")
            import sys
            sys.exit(0)
        return self.cells[i][j]

    def _init_pieces(self):
        # Initialize white pieces
        self.cells[0][0].set_piece(Rook(PieceColour.WHITE))
        self.cells[0][1].set_piece(Knight(PieceColour.WHITE))
        self.cells[0][2].set_piece(Bishop(PieceColour.WHITE))
        self.cells[0][3].set_piece(Queen(PieceColour.WHITE))
        self.cells[0][4].set_piece(King(PieceColour.WHITE))
        self.cells[0][5].set_piece(Bishop(PieceColour.WHITE))
        self.cells[0][6].set_piece(Knight(PieceColour.WHITE))
        self.cells[0][7].set_piece(Rook(PieceColour.WHITE))

        # Initialize white pawns
        for i in range(8):
            self.cells[1][i].set_piece(Pawn(PieceColour.WHITE))

        # Initialize black pieces
        self.cells[7][0].set_piece(Rook(PieceColour.BLACK))
        self.cells[7][1].set_piece(Knight(PieceColour.BLACK))
        self.cells[7][2].set_piece(Bishop(PieceColour.BLACK))
        self.cells[7][3].set_piece(Queen(PieceColour.BLACK))
        self.cells[7][4].set_piece(King(PieceColour.BLACK))
        self.cells[7][5].set_piece(Bishop(PieceColour.BLACK))
        self.cells[7][6].set_piece(Knight(PieceColour.BLACK))
        self.cells[7][7].set_piece(Rook(PieceColour.BLACK))

        # Initialize black pawns
        for i in range(8):
            self.cells[6][i].set_piece(Pawn(PieceColour.BLACK))
