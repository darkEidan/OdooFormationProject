from application.services.employee_service import EmployeeService
from api.cli.employee_cli import create_employee_cli, list_employees_cli


def main():
    service = EmployeeService()

    while True:
        print("\n==== HR Management ====")
        print("1. Create employee")
        print("2. Get employee")
        print("3. List employees")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            create_employee_cli(service)

        elif choice == "2":
            get_employee_cli(service)

        elif choice == "3":
            list_employees_cli(service)

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
