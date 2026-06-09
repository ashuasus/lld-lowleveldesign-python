from .iterator import Iterator


# Concrete Iterator - for Library
class LibraryIterator(Iterator):
    def __init__(self, books):
        self._books = books
        self._position = 0

    def has_next(self):
        return self._position < len(self._books)

    def next(self):
        book = self._books[self._position]
        self._position += 1
        return book
