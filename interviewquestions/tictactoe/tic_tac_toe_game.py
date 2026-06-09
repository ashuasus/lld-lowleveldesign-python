from collections import deque
from .model.board import Board
from .model.player import Player
from .model.playing_piece_x import PlayingPieceX
from .model.playing_piece_o import PlayingPieceO
from .model.game_status import GameStatus


class TicTacToeGame:
    def __init__(self):
        self.players = deque()
        self.game_board = None
        self.winner = None

    def initialize_game(self):
        # Creating 2 Players
        self.players = deque()
        cross_piece = PlayingPieceX()
        player1 = Player("Player1", cross_piece)

        noughts_piece = PlayingPieceO()
        player2 = Player("Player2", noughts_piece)

        self.players.append(player1)
        self.players.append(player2)

        # Initialize Board of size 3
        self.game_board = Board(3)

    def start_game(self):
        no_winner = True
        while no_winner:
            # Remove the player whose turn is and also put the player in the list back
            current_player = self.players.popleft()

            # Get the free space from the board
            self.game_board.print_board()
            free_spaces = self.game_board.get_free_cells()
            if not free_spaces:
                no_winner = False
                continue

            # Read the user input
            print("Player: " + current_player.name + " - Please enter [row, column]: ", end="")
            s = input()
            values = s.split(",")
            input_row = int(values[0])
            input_column = int(values[1])

            # Place the piece in the board
            valid_move = self.game_board.add_piece(input_row, input_column, current_player.playing_piece)
            if not valid_move:
                # Invalid Move: Player can not insert the piece into this cell
                print("Incorrect position chosen, try again!")
                self.players.appendleft(current_player)
                continue
            self.players.append(current_player)

            # Check if the valid move is a winning move or not
            is_winner = self.check_for_winner(input_row, input_column, current_player.playing_piece.piece_type)
            if is_winner:
                self.game_board.print_board()
                self.winner = current_player
                return GameStatus.WIN

        return GameStatus.DRAW

    def check_for_winner(self, row, column, piece_type):
        row_match = True
        column_match = True
        diagonal_match = True
        anti_diagonal_match = True

        # Check Row
        for i in range(self.game_board.size):
            if self.game_board.board[row][i] is None or self.game_board.board[row][i].piece_type != piece_type:
                row_match = False
                break

        # Check Column
        for i in range(self.game_board.size):
            if self.game_board.board[i][column] is None or self.game_board.board[i][column].piece_type != piece_type:
                column_match = False
                break

        # Check Diagonally
        i, j = 0, 0
        while i < self.game_board.size:
            if self.game_board.board[i][j] is None or self.game_board.board[i][j].piece_type != piece_type:
                diagonal_match = False
                break
            i += 1
            j += 1

        # Check Anti-Diagonally
        i, j = 0, self.game_board.size - 1
        while i < self.game_board.size:
            if self.game_board.board[i][j] is None or self.game_board.board[i][j].piece_type != piece_type:
                anti_diagonal_match = False
                break
            i += 1
            j -= 1

        return row_match or column_match or diagonal_match or anti_diagonal_match
