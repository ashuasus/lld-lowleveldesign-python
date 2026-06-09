from .player import Player
from .game import Game
from .position import Position
from .enums.piece_colour import PieceColour


def main():
    print("\n###### LLD of Chess Game Demo ######")
    p1_white = Player("Alice", PieceColour.WHITE)
    p2_black = Player("Bob", PieceColour.BLACK)

    game = Game(p1_white, p2_black)
    game.display()

    # Shortest Game: Fool's Mate Demo

    # Move 1: White[Pawn f2 -> f3]
    game.play_move(p1_white, Position(1, 5), Position(2, 5))
    game.display()

    # Move 2: Black[Pawn e7 -> e5]
    game.play_move(p2_black, Position(6, 4), Position(4, 4))
    game.display()

    # Move 3: White[Pawn g2 -> g4]
    game.play_move(p1_white, Position(1, 6), Position(3, 6))
    game.display()

    # Move 4: Black[Queen d8 -> h4]
    game.play_move(p2_black, Position(7, 3), Position(3, 7))
    game.display()

    # Move 5: White[Pawn a2 -> a3]
    game.play_move(p1_white, Position(1, 0), Position(2, 0))
    game.display()

    # Move 6: Black[Queen h4 -> e1] [Checkmate]
    game.play_move(p2_black, Position(3, 7), Position(0, 4))

    print("\nMoves History: ")
    game.display_moves_history()
    print("\nGame demo completed!")


if __name__ == "__main__":
    main()
