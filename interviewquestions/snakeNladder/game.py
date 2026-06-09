from collections import deque
from .board import Board
from .dice import Dice
from .player import Player


class Game:
    def __init__(self):
        self.board = None
        self.dice = None
        self.players_list = deque()
        self.winner = None
        self._initialize_game()

    def _initialize_game(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self._add_players()

    def _add_players(self):
        player1 = Player("Player-1", 0)
        player2 = Player("Player-2", 0)
        self.players_list.append(player1)
        self.players_list.append(player2)

    def start_game(self):
        while self.winner is None:
            # check whose turn now
            player_turn = self._find_player_turn()
            print("Player turn:" + player_turn.id + " current position is: " + str(player_turn.current_position))

            # roll the dice
            dice_numbers = self.dice.roll_dice()

            # get the new position
            player_new_position = player_turn.current_position + dice_numbers
            player_new_position = self._jump_check(player_new_position)
            player_turn.current_position = player_new_position

            print("Player turn:" + player_turn.id + " new Position is: " + str(player_new_position))
            # check for winning condition
            if player_new_position >= len(self.board.cells) * len(self.board.cells) - 1:
                self.winner = player_turn

        print("\n===> The Winner is:" + self.winner.id)

    def _find_player_turn(self):
        player_turns = self.players_list.popleft()
        self.players_list.append(player_turns)
        return player_turns

    def _jump_check(self, player_new_position):
        board_size = len(self.board.cells)
        if player_new_position > board_size * board_size - 1:
            return player_new_position

        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jump_by = "Ladder" if cell.jump.start < cell.jump.end else "Snake"
            print("[+] Jump done by: " + jump_by)
            return cell.jump.end
        return player_new_position
