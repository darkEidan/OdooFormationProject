import re
from domain.models.employee import Employee
from infrastructure.protocols.employee_repository_protocol import EmployeeRepositoryProtocol


class EmployeeService:

    def __init__(self, employee_repo : EmployeeRepositoryProtocol):
        self.repo = employee_repo

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def create_employee(self, employee : Employee):

        #Validate partially the mail address
        if not self._is_valid_email(employee.email):
            raise ValueError("Invalid email format")

        #Check for mail duplicate
        existing = self.repo.get_employee_by_email(employee.email)
        if existing:
            raise ValueError("Employee with this email already exists")

        return self.repo.create_employee(employee)

    def get_employee(self, employee_id):

        employee = self.repo.get_employee_by_id(employee_id)

        if employee is None:
            raise ValueError(f"Employee {employee_id} not found")

        return employee

    def list_employees(self):
        return self.repo.list_employees()


