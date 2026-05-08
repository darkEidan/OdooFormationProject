from domain.models.enums import EmployeeStatus
from typing import List, Optional
from datetime import date

class Employee:
    def __init__(
        self,
        employee_id: Optional[int],
        name: str,
        email: str,
        hire_date: date,
        status: EmployeeStatus,
        department_id: int,
        role_id: int
    ):
        self.id = employee_id
        self.name = name
        self.email = email
        self.hire_date = hire_date
        self.status = status
        self.department_id = department_id
        self.role_id = role_id

        # self.leaves: List["Leave"] = []
        # self.attendances: List["Attendance"] = []
        # self.benefits: List["EmployeeBenefit"] = []

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "hire_date": self.hire_date,
            "status": self.status.value,
            "department_id": self.department_id,
            "role_id": self.role_id
        }
