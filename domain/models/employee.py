from enums import EmployeeStatus
from attendance import Attendance
from leave import Leave
from typing import List
from datetime import date
from departement import Department
from role import Role
from benefit import EmployeeBenefit

class Employee:
    def __init__(
        self,
        employee_id: int,
        name: str,
        email: str,
        hire_date: date,
        status: EmployeeStatus,
        department: Department,
        role: Role
    ):
        self.id = employee_id
        self.name = name
        self.email = email
        self.hire_date = hire_date
        self.status = status
        self.department = department
        self.role = role

        self.leaves: List["Leave"] = []
        self.attendances: List["Attendance"] = []
        self.benefits: List["EmployeeBenefit"] = []

    # ===== Business methods =====

    def request_leave(self, leave: "Leave"):
        if leave.start_date < date.today():
            raise ValueError("Cannot request leave in the past")
        self.leaves.append(leave)

    def add_attendance(self, attendance: "Attendance"):
        self.attendances.append(attendance)

    def assign_benefit(self, benefit: "EmployeeBenefit"):
        self.benefits.append(benefit)
