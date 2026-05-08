import pytest
from datetime import datetime
from application.services.attendance_service import AttendanceService
from domain.models.attendance import Attendance
from infrastructure.fakes.fake_attendance_repository import FakeAttendanceRepo


def test_check_in_success():
    service = AttendanceService(FakeAttendanceRepo())

    result = service.check_in(1)

    assert result.is_open()


def test_check_in_fail_if_already_open():
    repo = FakeAttendanceRepo()
    repo.open_attendance = Attendance(1,1,datetime.now(),None)

    service = AttendanceService(repo)

    with pytest.raises(ValueError):
        service.check_in(1)


def test_check_out_success():
    repo = FakeAttendanceRepo()
    repo.open_attendance = Attendance(1, 1, datetime.now(), None)

    service = AttendanceService(repo)

    result = service.check_out(1)

    assert result.check_out is not None


def test_check_out_fail_if_no_open():
    service = AttendanceService(FakeAttendanceRepo())

    with pytest.raises(ValueError):
        service.check_out(1)


