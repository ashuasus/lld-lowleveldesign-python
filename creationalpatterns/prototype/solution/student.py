from .student_prototype import StudentPrototype


# Concrete prototype class
class Student(StudentPrototype):
    def __init__(self, id=None, name=None, branch=None, roll_no=None):
        self.id = id
        self.name = name
        self.branch = branch
        self.in_high_school = False
        self._roll_no = roll_no

    # setter method
    def set_in_high_school(self, in_high_school):
        self.in_high_school = in_high_school

    def clone(self):
        return Student(self.id, self.name, self.branch, self._roll_no)

    def print_details(self):
        print("=== Student Details ===")
        print(str(self) + ": ", end="")
        print("Id: " + str(self.id) + ", Name: " + str(self.name) + ", Branch: " + str(self.branch) + ", Roll No: " + str(self._roll_no) + ", In High School: " + str(self.in_high_school))
