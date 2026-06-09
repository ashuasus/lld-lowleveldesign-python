from .student import Student


# Client
def main():
    student_org = Student(1, "Aman", "CSE", 123)
    student_org.print_details()
    # create a clone of the student object
    student_clone = Student()
    student_clone.id = student_org.id
    student_clone.name = student_org.name
    student_clone.branch = student_org.branch
    # student_clone._roll_no = student_org._roll_no  # private field - accessible via name mangling in Python but logically restricted


if __name__ == "__main__":
    main()
