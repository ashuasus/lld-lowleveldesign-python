from .engineering_student_builder import EngineeringStudentBuilder
from .mba_student_builder import MBAStudentBuilder
from .student_registration_director import StudentRegistrationDirector


# Step 6: Client demonstration
def main():
    print("===== Builder Design Pattern =====")
    # Create director objects
    engg_student_director = StudentRegistrationDirector(EngineeringStudentBuilder())
    mba_student_director = StudentRegistrationDirector(MBAStudentBuilder())

    # Create students using different builders
    engineer_student = engg_student_director.create_student()
    mba_student = mba_student_director.create_student()

    # Print student details
    print("===> Student details:" + str(engineer_student))
    print("===> Student details:" + str(mba_student))


if __name__ == "__main__":
    main()
