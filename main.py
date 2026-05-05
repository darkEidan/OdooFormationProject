from application.services.department_service import DepartmentService
from application.services.employee_service import EmployeeService
from api.cli.employee_cli import create_employee_cli, list_employees_cli, get_employee_cli
from application.services.role_service import RoleService


def main():
    emp_service = EmployeeService()
    department_service = DepartmentService()
    role_service = RoleService()

    while True:
        print("\n==== HR Management ====")
        print("1. Create employee")
        print("2. Get employee")
        print("3. List employees")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            create_employee_cli(emp_service, department_service, role_service)

        elif choice == "2":
            get_employee_cli(emp_service)

        elif choice == "3":
            list_employees_cli(emp_service)

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
