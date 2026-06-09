# Step 1: Product class - The complex Student object being built
class Student:
    # Without Builder - Constructor overloading
    # Telescoping Constructor Problem - adding mandatory parameters
    def __init__(self, roll_number, age, name, branch,
                 father_name=None, mother_name=None,
                 subjects=None, mobile_no=None, email_id=None):
        self.roll_number = roll_number
        self.age = age
        self.name = name
        self.branch = branch
        self.father_name = father_name
        self.mother_name = mother_name
        self.subjects = subjects
        self.mobile_no = mobile_no
        self.email_id = email_id

    def print_details(self):
        print("=== Student Details ===")
        print(str(self) + ": ", end="")
        print("Id: " + str(self.roll_number) +
              ", Name: " + str(self.name) +
              ", Age: " + str(self.age) +
              ", Branch: " + str(self.branch) +
              ", Roll No: " + str(self.roll_number) +
              ", Father Name: " + str(self.father_name) +
              ", Mother Name: " + str(self.mother_name) +
              ", Subjects: " + str(self.subjects) +
              ", Mobile No: " + str(self.mobile_no) +
              ", Email Id: " + str(self.email_id))
