from creationalpatterns.builder.solution.student_builder import StudentBuilder


class MBAStudentBuilder(StudentBuilder):
    def set_subjects(self):
        self.subjects = [
            "Micro Economics",
            "Business Studies",
            "Operations Management",
            "Financial Management",
        ]
        return self
