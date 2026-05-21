from datetime import datetime
from domain.models.employee import Employee
from domain.models.enums import EmployeeStatus


def create_employee_cli(service, departments, roles):
    try:
        name = input("Name: ")
        email = input("Email: ")

        hire_date_str = input("Hire date (DD-MM-YYYY): ")
        hire_date = datetime.strptime(hire_date_str, "%d-%m-%Y").date()

        print("\nDepartments:")
        for d in departments:
            print(f"{d.id} - {d.name}")

        department_id = int(input("Department ID: "))
        if not any(d.id == department_id for d in departments):
            print("❌ Invalid department")
            return

        print("\nRoles:")
        for r in roles:
            print(f"{r.id} - {r.name} ({r.level})")

        role_id = int(input("Role ID: "))
        if not any(r.id == role_id for r in roles):
            print("❌ Invalid role")
            return

        employee = Employee(
            employee_id=None,
            name=name,
            email=email,
            hire_date=hire_date,
            status=EmployeeStatus.ACTIVE,
            department_id=department_id,
            role_id=role_id
        )

        employee = service.create_employee(employee)

        print("✅ Created:", employee)

    except ValueError:
        print("❌ Invalid input")

    except Exception as e:
        print("❌ Unexpected error:", e)

def get_employee_cli(service):
    try:
        employee_id = int(input("Enter employee ID: "))

        employee = service.get_employee(employee_id)

        if employee:
            print("\n👤 Employee found:")
            print(f"ID: {employee.id}")
            print(f"Name: {employee.name}")
            print(f"Email: {employee.email}")
            print(f"Status: {employee.status.value}")
            print(f"Department ID: {employee.department_id}")
            print(f"Role ID: {employee.role_id}")
        else:
            print("⚠️ Employee not found.")

    except ValueError:
        print("❌ Please enter a valid number.")

    except Exception as e:
        print("❌ Unexpected error:", e)

def list_employees_cli(service):
    try:
        employees = service.list_employees()

        if not employees:
            print("⚠️ No employees found.")
            return

        print("\n📋 Employees:\n")

        for emp in employees:
            print(f"{emp.id} - {emp.name} ({emp.email})")

    except Exception as e:
        print("❌ Unexpected error:", e)
