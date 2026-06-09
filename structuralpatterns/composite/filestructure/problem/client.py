from .directory import Directory
from .file import File


# Client Code
def main():
    movie_directory = Directory("Movies")

    rental_receipt = File("RentalReceipt")
    movie_directory.add(rental_receipt)

    comedy_movie_directory = Directory("ComedyMovies")
    dumb_and_dumber = File("DumbAndDumber")
    comedy_movie_directory.add(dumb_and_dumber)
    movie_directory.add(comedy_movie_directory)

    movie_directory.print_contents()


if __name__ == "__main__":
    main()
