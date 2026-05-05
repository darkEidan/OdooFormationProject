from application.services.employee_service import EmployeeService

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
            name = input("Name: ")
            email = input("Email: ")
            hire_date = input("Hire date (YYYY-MM-DD): ")
            department_id = int(input("Department ID: "))
            role_id = int(input("Role ID: "))

            employee = service.create_employee(
                name, email, hire_date, department_id, role_id
            )

            print("✅ Created:", employee)

        elif choice == "2":
            employee_id = int(input("Enter employee ID: "))
            employee = service.get_employee(employee_id)

            print(employee if employee else "❌ Not found")

        elif choice == "3":
            employees = service.list_employees()

            for emp in employees:
                print(f"{emp['id']} - {emp['name']}")

        elif choice == "0":
            break

        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
