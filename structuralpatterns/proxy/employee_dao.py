from abc import ABC, abstractmethod


# Subject interface - common interface for RealSubject and Proxy
class EmployeeDao(ABC):
    @abstractmethod
    def get_employee_info(self, emp_id):
        pass

    @abstractmethod
    def create_employee(self, obj):
        pass
