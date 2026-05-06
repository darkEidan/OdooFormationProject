from typing import Optional
from domain.models.enums import LeaveStatus, LeaveType
from datetime import date


class Leave:
    def __init__(
        self,
        id: Optional[int],
        employee_id: int,
        start_date: date,
        end_date: date,
        leave_type: LeaveType = LeaveType.PAID,
        status: LeaveStatus = LeaveStatus.PENDING
    ):
        self.id = id
        self.employee_id = employee_id
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def approve(self):
        if self.status != LeaveStatus.PENDING:
            raise ValueError("Only pending leaves can be approved")

        self.status = LeaveStatus.APPROVED

    def reject(self):
        if self.status != LeaveStatus.PENDING:
            raise ValueError("Only pending leaves can be rejected")

        self.status = LeaveStatus.REJECTED

    def duration(self) -> int:

        if not self.is_valid():
            raise ValueError("Invalid leave dates")

        return (self.end_date - self.start_date).days + 1

    def is_valid(self) -> bool:
        return self.start_date <= self.end_date

    def validate_for_request(self, today: date):
        if self.start_date < today:
            raise ValueError("Leave cannot start in the past")

        if not self.is_valid():
            raise ValueError("Invalid leave dates")
