from employee import Employee
from datetime import datetime, date

class Attendance:
    def __init__(
        self,
        attendance_id: int,
        employee: Employee,
        attendance_date: date,
        check_in: datetime,
        check_out: datetime
    ):
        self.attendance_id = attendance_id
        self.employee = employee
        self.attendance_date = attendance_date
        self.check_in = check_in
        self.check_out = check_out

    def get_worked_hours(self) -> float:
        if not self.check_out:
            return 0
        delta = self.check_out - self.check_in
        return delta.total_seconds() / 3600

