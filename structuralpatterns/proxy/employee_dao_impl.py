from .employee_dao import EmployeeDao


# RealSubject - the actual employee object that does the real work
class EmployeeDaoImpl(EmployeeDao):
    def get_employee_info(self, emp_id):
        print("Fetching employee info for ID: " + str(emp_id))

    def create_employee(self, obj):
        print("Creating employee: " + str(obj))
