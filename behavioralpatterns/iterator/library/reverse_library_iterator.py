from .iterator import Iterator


# Concrete Iterator - for Library
class ReverseLibraryIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._position = len(books) - 1

    def has_next(self):
        return self._position >= 0 and self._books[self._position] is not None

    def next(self):
        if not self.has_next():
            return None
        book = self._books[self._position]
        self._position -= 1
        return book
