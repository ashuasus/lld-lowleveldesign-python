from .book_collection import BookCollection
from .library_iterator import LibraryIterator
from .reverse_library_iterator import ReverseLibraryIterator


# Concrete Aggregate
class Library(BookCollection):
    def __init__(self, books):
        self._books = books

    def create_iterator(self):
        return LibraryIterator(self._books)

    def create_reverse_iterator(self):
        return ReverseLibraryIterator(self._books)
