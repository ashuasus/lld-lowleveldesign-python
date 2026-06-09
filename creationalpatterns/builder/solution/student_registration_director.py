from .engineering_student_builder import EngineeringStudentBuilder
from .mba_student_builder import MBAStudentBuilder


# Step 5: Director class for common student registration processes
class StudentRegistrationDirector:
    def __init__(self, student_builder):
        self.student_builder = student_builder

    def create_student(self):
        if isinstance(self.student_builder, EngineeringStudentBuilder):
            return self._create_engineering_student()
        elif isinstance(self.student_builder, MBAStudentBuilder):
            return self._create_mba_student()
        return None

    def _create_engineering_student(self):
        return (self.student_builder
                .set_roll_number(1)
                .set_age(22)
                .set_name("John")
                .set_father_name("Paul")
                .set_mother_name("Jane")
                .set_branch("Computer Science and Engineering")
                .set_subjects()
                .build())

    def _create_mba_student(self):
        return (self.student_builder
                .set_roll_number(2)
                .set_age(24)
                .set_name("Sarah")
                .set_father_name("Gabriel")
                .set_mother_name("Taylor")
                .set_branch("Business Administration")
                .set_subjects()
                .set_mobile_no("9876543210")
                .set_email_id("sarahgabriel@iitb.com")
                .build())
