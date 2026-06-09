from .character import Character


def main():
    print("Word Processor: Issue Demo")
    # Data: "Hello World"
    # Total 11 characters

    # Create 11 character objects
    object1 = Character('H', "Arial", 10, 0, 0)
    object2 = Character('e', "Arial", 10, 0, 1)
    object3 = Character('l', "Arial", 10, 0, 2)
    object4 = Character('l', "Arial", 10, 0, 3)
    object5 = Character('o', "Arial", 10, 0, 4)
    object6 = Character(' ', "Arial", 10, 0, 5)
    object7 = Character('W', "Arial", 10, 0, 6)
    object8 = Character('o', "Arial", 10, 0, 7)
    object9 = Character('r', "Arial", 10, 0, 8)
    object10 = Character('l', "Arial", 10, 0, 9)
    object11 = Character('d', "Arial", 10, 0, 10)


if __name__ == "__main__":
    main()
