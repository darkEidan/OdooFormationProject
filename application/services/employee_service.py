import re
from infrastructure.repositories.employee_repository import EmployeeRepository


class EmployeeService:

    def __init__(self):
        self.repo = EmployeeRepository()

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def create_employee(self, name, email, hire_date, department_id, role_id):

        #Validate partially the mail address
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")

        #Check for mail duplicate
        existing = self.repo.get_employee_by_email(email)
        if existing:
            raise ValueError("Employee with this email already exists")

        return self.repo.create_employee(
            name,
            email,
            hire_date,
            "active",
            department_id,
            role_id
        )

    def get_employee(self, employee_id):
        return self.repo.get_employee_by_id(employee_id)

    def list_employees(self):
        return self.repo.list_employees()


