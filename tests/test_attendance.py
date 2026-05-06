from domain.models.attendance import Attendance
from datetime import datetime


def test_is_open():
    att = Attendance(None, 1, datetime.now(), None)
    assert att.is_open() is True


def test_worked_hours():
    check_in = datetime(2024, 1, 1, 8, 0)
    check_out = datetime(2024, 1, 1, 16, 0)

    att = Attendance(None, 1, check_in, check_out)

    assert att.get_worked_hours() == 8.0