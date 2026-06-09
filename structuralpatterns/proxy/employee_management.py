from .employee_dao_proxy import EmployeeDaoProxy
from .employee_do import EmployeeDo


# Client
def main():
    print("===== Proxy Design Pattern =====")
    user_proxy_obj = EmployeeDaoProxy("USER")
    user_proxy_obj.get_employee_info(1)  # access granted
    user_proxy_obj.create_employee(EmployeeDo())  # access denied


if __name__ == "__main__":
    main()
