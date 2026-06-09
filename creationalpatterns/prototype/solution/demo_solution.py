from .student import Student


# Client
def main():
    print("======= Prototype Design Pattern ======")

    # Create initial prototypes (expensive operations)
    student = Student(5, "Rita", "CSE", 224)
    student.print_details()
    # Clone objects (fast operations)
    student_clone = student.clone()
    student_clone.set_in_high_school(True)
    student_clone.print_details()
    print("Same object? " + str(student is student_clone))


if __name__ == "__main__":
    main()
