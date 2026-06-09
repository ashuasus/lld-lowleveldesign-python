from .book import Book
from .library import Library


# Client
def main():
    print("\n###### Iterator Design Pattern ######")

    # Create Library
    library = get_library()

    # Forward iteration
    iterator = library.create_iterator()
    print("\n==> Forward iteration:")
    display_library(iterator)

    # Reverse iteration
    reverse_iterator = library.create_reverse_iterator()
    print("\n==> Reverse iteration:")
    display_library(reverse_iterator)


def get_library():
    books = [
        Book("To Kill a Mockingbird", "Harper Lee", "978-0-74-7356-5"),
        Book("The Great Gatsby", "F. Scott Fitzgerald", "778-0-24-7156-5"),
        Book("The Catcher in the Rye", "J.D. Salinger", "333-0-28-7446-8"),
        Book("The Hobbit", "J.R.R. Tolkien", "783-0-14-1951-8"),
        Book("Rich Dad Poor Dad", "Robert Kiyosaki", "183-0-12-1491-8"),
        Book("Pride and Prejudice", "Jane Austen", "289-0-12-1678-8")
    ]
    library = Library(books)
    return library


def display_library(iterator):
    while iterator.has_next():
        book = iterator.next()
        print(book)


if __name__ == "__main__":
    main()
