from .employee_dao import EmployeeDao
from .employee_dao_impl import EmployeeDaoImpl


# Proxy class - controls access to RealEmployee
class EmployeeDaoProxy(EmployeeDao):
    def __init__(self, client_role):
        self._emp_dao_obj = EmployeeDaoImpl()
        self._client_role = client_role

    def get_employee_info(self, emp_id):
        if self._client_role in ("ADMIN", "USER"):
            self._emp_dao_obj.get_employee_info(emp_id)
        else:
            raise RuntimeError("Access Denied")

    def create_employee(self, obj):
        if self._client_role == "ADMIN":
            self._emp_dao_obj.create_employee(obj)
        else:
            raise RuntimeError("Access Denied")
