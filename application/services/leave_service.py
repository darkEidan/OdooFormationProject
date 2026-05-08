from infrastructure.protocols.leave_repository_protocol import LeaveRepositoryProtocol
from domain.models.leave import Leave
from datetime import date

class LeaveService:

    def __init__(self, leave_repo : LeaveRepositoryProtocol):
        self.repo = leave_repo

    def request_leave(self, leave: Leave):

        leave.validate_for_request(date.today())

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

        leave.approve()

        return self.repo.update(leave)

    def reject_leave(self, leave_id: int):
        leave = self.repo.get_by_id(leave_id)

        if not leave:
            raise ValueError("Leave not found")

        leave.reject()

        return self.repo.update(leave)

    def list_employee_leaves(self, employee_id: int):
        return self.repo.list_by_employee(employee_id)
