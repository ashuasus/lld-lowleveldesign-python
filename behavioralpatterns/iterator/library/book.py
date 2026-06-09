# Book class representing individual books in a library
class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._price = 0

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_isbn(self):
        return self._isbn

    def get_price(self):
        return self._price

    def __str__(self):
        return "Book [Title=" + self._title + ", Author=" + self._author + ", ISBN=" + self._isbn + "]"
