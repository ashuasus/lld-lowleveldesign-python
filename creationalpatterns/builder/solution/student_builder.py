from abc import ABC, abstractmethod


# Step 2: Abstract Builder interface
class StudentBuilder(ABC):
    def __init__(self):
        # mandatory fields
        self.roll_number = None
        self.age = None
        self.name = None
        self.branch = None
        # optional fields
        self.father_name = None
        self.mother_name = None
        self.subjects = None
        self.mobile_no = None
        self.email_id = None

    def set_roll_number(self, roll_number):
        self.roll_number = roll_number
        return self

    def set_age(self, age):
        self.age = age
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_branch(self, branch):
        self.branch = branch
        return self

    def set_father_name(self, father_name):
        self.father_name = father_name
        return self

    def set_mother_name(self, mother_name):
        self.mother_name = mother_name
        return self

    def set_mobile_no(self, mobile_no):
        self.mobile_no = mobile_no
        return self

    def set_email_id(self, email_id):
        self.email_id = email_id
        return self

    @abstractmethod
    def set_subjects(self):
        pass

    # Build method
    def build(self):
        from .student import Student
        return Student(self)
