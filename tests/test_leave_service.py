import pytest
from datetime import date
from application.services.leave_service import LeaveService
from domain.models.enums import LeaveStatus,LeaveType
from infrastructure.fakes.fake_leave_repository import FakeLeaveRepo
from domain.models.leave import Leave

def build_leave(start=date(2027, 1, 1), end=date(2027, 1, 5)):
    return Leave(
        id=None,
        employee_id=1,
        start_date=start,
        end_date=end,
        leave_type=LeaveType.PAID
    )

def test_request_leave_success():
    service = LeaveService(FakeLeaveRepo())
    leave = build_leave()
    result = service.request_leave(leave)

    assert result.id is not None


def test_request_leave_invalid_dates():
    service = LeaveService(FakeLeaveRepo())

    leave = build_leave(date(2027, 1, 5), date(2027, 1, 1))

    with pytest.raises(ValueError):
        service.request_leave(leave)


def test_request_leave_overlap():
    service = LeaveService(FakeLeaveRepo())

    existing = build_leave(date(2027, 1, 1), date(2027, 1, 5))
    service.repo.create(existing)

    new_leave = build_leave(date(2027, 1, 3), date(2027, 1, 6))

    with pytest.raises(ValueError):
        service.request_leave(new_leave)


def test_approve_leave_success():
    service = LeaveService(FakeLeaveRepo())

    leave = service.request_leave(build_leave())

    result = service.approve_leave(leave.id)

    assert result.status == LeaveStatus.APPROVED


def test_approve_leave_not_found():
    service = LeaveService(FakeLeaveRepo())

    with pytest.raises(ValueError):
        service.approve_leave(999)


def test_approve_leave_not_pending():
    service = LeaveService(FakeLeaveRepo())

    leave = service.request_leave(build_leave())
    leave.status = LeaveStatus.APPROVED

    with pytest.raises(ValueError):
        service.approve_leave(leave.id)


def test_reject_leave_success():
    service = LeaveService(FakeLeaveRepo())

    leave = service.request_leave(build_leave())

    result = service.reject_leave(leave.id)

    assert result.status == LeaveStatus.REJECTED
