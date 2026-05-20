from typing import Protocol


class EmployeeRepositoryProtocol(Protocol):

    def create_employee(self, employee):
        ...

    def get_employee_by_id(self, employee_id):
        ...

    def list_employees(self):
        ...

    def get_employee_by_email(self, email):
        ...

