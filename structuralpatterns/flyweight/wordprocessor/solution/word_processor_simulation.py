from .letter_factory import LetterFactory


# Client – supplies extrinsic state when using flyweights
def main():
    print("====== Flyweight Design Pattern ======")
    # Data: "Hello World"
    # Total 11 characters (including space)

    # Create 11 character objects and provide display position(extrinsic state) at runtime
    object1 = LetterFactory.crate_letter('H')
    object1.display(0, 0)

    object2 = LetterFactory.crate_letter('e')
    object2.display(0, 1)

    object3 = LetterFactory.crate_letter('l')
    object3.display(0, 2)

    object4 = LetterFactory.crate_letter('l')
    object4.display(0, 3)

    object5 = LetterFactory.crate_letter('o')
    object5.display(0, 4)

    object6 = LetterFactory.crate_letter(' ')
    object6.display(0, 5)

    object7 = LetterFactory.crate_letter('W')
    object7.display(0, 6)

    object8 = LetterFactory.crate_letter('o')
    object8.display(0, 7)

    object9 = LetterFactory.crate_letter('r')
    object9.display(0, 8)

    object10 = LetterFactory.crate_letter('l')
    object10.display(0, 9)

    object11 = LetterFactory.crate_letter('d')
    object11.display(0, 10)

    # Total characters created: 8 - because we are reusing the same object
    print("Total characters created: " + str(LetterFactory.get_total_characters()))


if __name__ == "__main__":
    main()
