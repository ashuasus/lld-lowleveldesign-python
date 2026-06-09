from .i_letter import ILetter


# Concrete Flyweight (Class) - implements the Flyweight interface and stores intrinsic state
class DocumentCharacter(ILetter):
    def __init__(self, character, font_type, size):
        # intrinsic data - shared data - common to all objects
        self._character = character
        self._font_type = font_type
        self._size = size

    def display(self, row, column):
        # display the character of particular font and size at given location
        print("Displaying " + str(self._character) + " at row " + str(row) + " and column " + str(column))
