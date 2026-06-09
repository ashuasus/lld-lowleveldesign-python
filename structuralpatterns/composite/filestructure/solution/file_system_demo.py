from .file import File
from .directory import Directory


# Step 4: Client code with Composite Pattern
def main():
    print("======= Composite Design Pattern ======")

    # Create files
    receipt = File("receipt.pdf")
    invoice = File("invoice.pdf")
    torrent_links = File("torrentLinks.txt")
    tom_cruise = File("tomCruise.jpg")
    dumb_and_dumber = File("DumbAndDumber.mp4")
    hangover_i = File("HangoverI.mp4")

    # Create directories
    movies_directory = Directory("Movies")
    comedy_movie_directory = Directory("ComedyMovies")

    # Build the tree structure hierarchically
    movies_directory.add(receipt)
    movies_directory.add(invoice)
    movies_directory.add(torrent_links)
    movies_directory.add(tom_cruise)
    movies_directory.add(comedy_movie_directory)
    comedy_movie_directory.add(dumb_and_dumber)
    comedy_movie_directory.add(hangover_i)

    # Display full structure
    movies_directory.print_contents()


if __name__ == "__main__":
    main()
