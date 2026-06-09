from .tic_tac_toe_game import TicTacToeGame
from .model.game_status import GameStatus


def main():
    print("\n===>>> TicTacToe Game\n")
    game = TicTacToeGame()
    game.initialize_game()
    status = game.start_game()
    print("\n===>>> GAME OVER: ", end="")
    if status == GameStatus.WIN:
        print(game.winner.name + " won the game")
    elif status == GameStatus.DRAW:
        print(" Its a Draw!")
    else:
        print(" Game Ends")


if __name__ == "__main__":
    main()
