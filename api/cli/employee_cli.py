from datetime import datetime

from application.services.employee_service import EmployeeService
from application.services.role_service import RoleService
from domain.models.employee import Employee
from domain.models.enums import EmployeeStatus
from application.services.department_service import DepartmentService
from api.cli.department_cli import list_departments_cli
from role_cli import list_roles_cli


def create_employee_cli(emp_serv : EmployeeService, depart_serv : DepartmentService, role_serv : RoleService):
    try:

        name = input("Name: ")
        email = input("Email: ")

        hire_date_str = input("Hire date (DD-MM-YYYY): ")
        hire_date = datetime.strptime(hire_date_str, "%d-%m-%Y").date()

        print("Department List")
        print("---------------")
        list_departments_cli(depart_serv)
        department_id = int(input("Department ID: "))

        print("Role List")
        print("---------")
        list_roles_cli(role_serv)
        role_id = int(input("Role ID: "))

        employee = Employee(
            employee_id=None,
            name=name,
            email=email,
            hire_date=hire_date,
            status=EmployeeStatus.ACTIVE,
            department_id=department_id,
            role_id=role_id
        )

        employee = emp_serv.create_employee(employee)

        print("✅ Created:", employee)

    except ValueError as e:
        print("❌", e)

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
