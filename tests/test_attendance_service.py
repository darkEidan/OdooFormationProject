import pytest
from datetime import datetime
from application.services.attendance_service import AttendanceService
from domain.models.attendance import Attendance


class FakeRepo:

    def __init__(self):
        self.open_attendance = None

    def get_open_attendance(self, employee_id):
        return self.open_attendance

    def check_in(self, employee_id, check_in):
        return Attendance(1, employee_id, check_in, None)

    def check_out(self, employee_id, check_out):
        return Attendance(1, employee_id, datetime.now(), check_out)


def test_check_in_success():
    service = AttendanceService()
    service.repo = FakeRepo()

    result = service.check_in(1)

    assert result.is_open()


def test_check_in_fail_if_already_open():
    service = AttendanceService()
    fake_repo = FakeRepo()
    fake_repo.open_attendance = Attendance(1, 1, datetime.now(), None)

    service.repo = fake_repo

    with pytest.raises(ValueError):
        service.check_in(1)


def test_check_out_success():
    service = AttendanceService()
    fake_repo = FakeRepo()
    fake_repo.open_attendance = Attendance(1, 1, datetime.now(), None)

    service.repo = fake_repo

    result = service.check_out(1)

    assert result.check_out is not None


def test_check_out_fail_if_no_open():
    service = AttendanceService()
    service.repo = FakeRepo()

    with pytest.raises(ValueError):
        service.check_out(1)


