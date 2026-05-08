from domain.models.attendance import Attendance
from datetime import datetime

class FakeAttendanceRepo:

    def __init__(self):
        self.open_attendance = None

    def get_open_attendance(self, employee_id):
        return self.open_attendance

    def check_in(self, employee_id, check_in):
        self.open_attendance = Attendance(
            1,
            employee_id,
            check_in,
            None
        )

        return self.open_attendance

    def check_out(self, employee_id, check_out):
        if not self.open_attendance:
            return None

        self.open_attendance.check_out = check_out

        result = self.open_attendance

        self.open_attendance = None

        return result   

    def list_by_employee(self, employee_id):
        ...