class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn

    @staticmethod
    def get_books():
        return [
            Book("To Kill a Mockingbird", "Harper Lee", "978-0-74-7356-5"),
            Book("The Great Gatsby", "F. Scott Fitzgerald", "778-0-24-7156-5"),
            Book("The Catcher in the Rye", "J.D. Salinger", "333-0-28-7446-8"),
            Book("The Hobbit", "J.R.R. Tolkien", "783-0-14-1951-8"),
            Book("Rich Dad Poor Dad", "Robert Kiyosaki", "183-0-12-1491-8"),
            Book("Pride and Prejudice", "Jane Austen", "289-0-12-1678-8")
        ]

    def __str__(self):
        return "Book [Tittle='" + self._title + ", Author=" + self._author + ", age=" + "ISBN=" + self._isbn + "]"
