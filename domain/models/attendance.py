from datetime import datetime, date, timedelta
from typing import Optional


class Attendance:

    def __init__(
        self,
        attendance_id: Optional[int],
        employee_id: int,
        work_date : date,
        check_in: datetime,
        check_out: Optional[datetime] = None
    ):
        self.id = attendance_id
        self.employee_id = employee_id
        self.work_date = work_date
        self.check_in = check_in
        self.check_out = check_out

    def is_open(self) -> bool:
        return self.check_out is None

    def get_worked_hours(self) -> float:
        if not self.check_out:
            return 0.0

        delta : timedelta = self.check_out - self.check_in
        return round(delta.total_seconds() / 3600,2)
