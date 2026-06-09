from .board import Board
from .move import Move
from .enums.game_status import GameStatus
from .enums.piece_colour import PieceColour
from .pieces.king import King


class Game:
    def __init__(self, player1, player2):
        self._player1 = player1
        self._player2 = player2
        self._board = Board()
        if player1.get_playing_side() == PieceColour.WHITE:
            self._current_turn = player1
        else:
            self._current_turn = player2
        self._status = GameStatus.IN_PROGRESS
        self._moves_history = []

    def play_move(self, player, start, end):
        start_cell = self._board.get_cell(start)
        end_cell = self._board.get_cell(end)
        move = Move(player, start_cell, end_cell)
        return self._make_move(move, player)

    def _make_move(self, move, player):
        start_piece = move.get_start().get_piece()
        end_piece = move.get_end().get_piece()

        if start_piece is None:
            return False
        if start_piece.get_colour() != player.get_playing_side():
            return False
        if not start_piece.is_valid_move(self._board, move.get_start(), move.get_end()):
            return False

        if end_piece is not None:
            end_piece.set_captured(True)
            move.set_piece_killed(end_piece)

        move.set_piece_moved(start_piece)
        move.get_end().set_piece(start_piece)
        move.get_start().set_piece(None)

        self._moves_history.append(move)

        if isinstance(end_piece, King):
            print("\n===>>> Its a Checkmate!!!")
            if player.get_playing_side() == PieceColour.WHITE:
                self.set_status(GameStatus.WHITE_WIN)
                print("===>>> Game Status: " + str(self.get_status()))
            else:
                self.set_status(GameStatus.BLACK_WIN)
                print("===>>> Game Status: " + str(self.get_status()))

        if self._current_turn == self._player1:
            self._current_turn = self._player2
        else:
            self._current_turn = self._player1

        return True

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_board(self):
        return self._board

    def set_board(self, board):
        self._board = board

    def display_moves_history(self):
        for move in self._moves_history:
            print(move)

    def display(self):
        print("\nCurrent turn: " + str(self._current_turn))
        print("Game status: " + str(self._status))
