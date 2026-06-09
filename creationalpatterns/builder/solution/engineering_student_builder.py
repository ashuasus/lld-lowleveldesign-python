from .student_builder import StudentBuilder


# Step 3: Concrete Builder for Engineering Students
class EngineeringStudentBuilder(StudentBuilder):
    # Engineering-specific methods
    def set_subjects(self):
        engg_subjects_list = []
        engg_subjects_list.append("Operating Systems")
        engg_subjects_list.append("Computer Architecture")
        engg_subjects_list.append("Data Structures")
        engg_subjects_list.append("DBMS")
        self.subjects = engg_subjects_list
        return self
