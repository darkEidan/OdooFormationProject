from infrastructure.repositories.leave_repository import LeaveRepository
from domain.models.leave import Leave
from domain.models.enums import LeaveStatus, LeaveType


class LeaveService:

    def __init__(self):
        self.repo = LeaveRepository()

    def request_leave(self, leave: Leave):

        if leave.start_date < date.today():
            raise ValueError("Leave cannot start in the past")

        if not leave.is_valid():
            raise ValueError("Invalid leave dates")

        # Find overlapping leave.
        overlapping = self.repo.find_overlapping(
            leave.employee_id,
            leave.start_date,
            leave.end_date
        )

        if overlapping:
            raise ValueError("Leave request overlaps with existing leave")

        return self.repo.create(leave)

    def approve_leave(self, leave_id: int):
        leave = self.repo.get_by_id(leave_id)

        if not leave:
            raise ValueError("Leave not found")

        if leave.status != LeaveStatus.PENDING:
            raise ValueError("Only pending leaves can be approved")

        return self.repo.update_status(leave_id, LeaveStatus.APPROVED)

    def reject_leave(self, leave_id: int):
        leave = self.repo.get_by_id(leave_id)

        if not leave:
            raise ValueError("Leave not found")

        if leave.status != LeaveStatus.PENDING:
            raise ValueError("Only pending leaves can be rejected")

        return self.repo.update_status(leave_id, LeaveStatus.REJECTED)

    def list_employee_leaves(self, employee_id: int):
        return self.repo.list_by_employee(employee_id)
