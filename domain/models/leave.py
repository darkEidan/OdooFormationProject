from employee import Employee
from enums import LeaveStatus
from datetime import date

class Leave:
    def __init__(
        self,
        leave_id: int,
        employee: Employee,
        leave_type: str,
        start_date: date,
        end_date: date,
        status: LeaveStatus = LeaveStatus.PENDING
    ):
        self.leave_id = leave_id
        self.employee = employee
        self.leave_type = leave_type
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def approve(self):
        self.status = LeaveStatus.APPROVED

    def reject(self):
        self.status = LeaveStatus.REJECTED
