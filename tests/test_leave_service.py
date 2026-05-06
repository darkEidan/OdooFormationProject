import pytest
from datetime import date

from application.services.leave_service import LeaveService
from domain.models.leave import Leave
from domain.models.enums import LeaveStatus, LeaveType


class FakeLeaveRepo:

    def __init__(self):
        self.leaves = []
        self.next_id = 1

    def create(self, leave):
        leave.id = self.next_id
        self.next_id += 1
        self.leaves.append(leave)
        return leave

    def get_by_id(self, leave_id):
        for l in self.leaves:
            if l.id == leave_id:
                return l
        return None

    def list_by_employee(self, employee_id):
        return [l for l in self.leaves if l.employee_id == employee_id]

    def update_status(self, leave_id, status):
        leave = self.get_by_id(leave_id)
        if leave:
            leave.status = status
        return leave

    def find_overlapping(self, employee_id, start_date, end_date):
        return [
            l for l in self.leaves
            if l.employee_id == employee_id
            and not (l.end_date < start_date or l.start_date > end_date)
        ]

def build_leave(start=date(2027, 1, 1), end=date(2027, 1, 5)):
    return Leave(
        id=None,
        employee_id=1,
        start_date=start,
        end_date=end,
        leave_type=LeaveType.PAID
    )


def test_request_leave_success():
    service = LeaveService()
    service.repo = FakeLeaveRepo()

    leave = build_leave()
    result = service.request_leave(leave)

    assert result.id is not None


def test_request_leave_invalid_dates():
    service = LeaveService()
    service.repo = FakeLeaveRepo()

    leave = build_leave(date(2027, 1, 5), date(2027, 1, 1))

    with pytest.raises(ValueError):
        service.request_leave(leave)


def test_request_leave_overlap():
    service = LeaveService()
    fake_repo = FakeLeaveRepo()
    service.repo = fake_repo

    existing = build_leave(date(2027, 1, 1), date(2027, 1, 5))
    fake_repo.create(existing)

    new_leave = build_leave(date(2027, 1, 3), date(2027, 1, 6))

    with pytest.raises(ValueError):
        service.request_leave(new_leave)


def test_approve_leave_success():
    service = LeaveService()
    fake_repo = FakeLeaveRepo()
    service.repo = fake_repo

    leave = fake_repo.create(build_leave())

    result = service.approve_leave(leave.id)

    assert result.status == LeaveStatus.APPROVED


def test_approve_leave_not_found():
    service = LeaveService()
    service.repo = FakeLeaveRepo()

    with pytest.raises(ValueError):
        service.approve_leave(999)


def test_approve_leave_not_pending():
    service = LeaveService()
    fake_repo = FakeLeaveRepo()
    service.repo = fake_repo

    leave = fake_repo.create(build_leave())
    leave.status = LeaveStatus.APPROVED

    with pytest.raises(ValueError):
        service.approve_leave(leave.id)


def test_reject_leave_success():
    service = LeaveService()
    fake_repo = FakeLeaveRepo()
    service.repo = fake_repo

    leave = fake_repo.create(build_leave())

    result = service.reject_leave(leave.id)

    assert result.status == LeaveStatus.REJECTED
