from .book import Book


def main():
    print("\n###### Problem without Iterator Pattern Demo ######")
    # Client has access to the entire book list in the library
    book_list = Book.get_books()
    for book in book_list:
        print(book)


if __name__ == "__main__":
    main()
