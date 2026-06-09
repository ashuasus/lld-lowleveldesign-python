# Step 1: Product class - Complex Student object
class Student:
    # Constructor - only builder can create
    def __init__(self, builder):
        self.roll_number = builder.roll_number
        self.age = builder.age
        self.name = builder.name
        self.branch = builder.branch
        self.father_name = builder.father_name
        self.mother_name = builder.mother_name
        self.subjects = builder.subjects
        self.mobile_no = builder.mobile_no
        self.email_id = builder.email_id

    def __str__(self):
        return (" roll number: " + str(self.roll_number) +
                " age: " + str(self.age) +
                " name: " + str(self.name) +
                " branch: " + str(self.branch) +
                " father name: " + str(self.father_name) +
                " mother name: " + str(self.mother_name) +
                " subjects: " + str(self.subjects[0]) + "," + str(self.subjects[1]) + "," + str(self.subjects[2]) +
                " mobile no: " + str(self.mobile_no) +
                " email id: " + str(self.email_id))
