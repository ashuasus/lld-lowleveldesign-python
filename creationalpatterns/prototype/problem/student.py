# Concrete Class - Whose clone is to be created
class Student:
    def __init__(self, id=None, name=None, branch=None, roll_no=None):
        self.id = id
        self.name = name
        self.branch = branch
        self._roll_no = roll_no

    def print_details(self):
        print("=== Student Details ===")
        print(str(self) + ": ", end="")
        print("Id: " + str(self.id) + ", Name: " + str(self.name) + ", Branch: " + str(self.branch) + ", Roll No: " + str(self._roll_no))
