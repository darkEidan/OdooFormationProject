from infrastructure.repositories.base_repository import BaseRepository
from infrastructure.queries.attendance_queries import AttendanceQueries
from domain.models.attendance import Attendance


class AttendanceRepository(BaseRepository):

    def _map(self, row):
        if row is None:
            return None
        return Attendance(
            row["id"],
            row["employee_id"],
            row["check_in"],
            row["check_out"]
        )

    def check_in(self, employee_id, check_in):
        row = self._execute(AttendanceQueries.INSERT_CHECK_IN,{"employee_id": employee_id, "check_in": check_in},fetch_one=True)
        return self._map(row)

    def check_out(self, employee_id, check_out):
        row = self._execute(
            AttendanceQueries.UPDATE_CHECK_OUT,{"employee_id": employee_id, "check_out": check_out},fetch_one=True)
        return self._map(row)

    def get_open_attendance(self, employee_id):
        row = self._execute(
            AttendanceQueries.SELECT_OPEN_ATTENDANCE,{"employee_id": employee_id},fetch_one=True)
        return self._map(row)

    def list_by_employee(self, employee_id):
        rows = self._execute(
            AttendanceQueries.SELECT_BY_EMPLOYEE,{"employee_id": employee_id},fetch_all=True)
        return [self._map(r) for r in rows]
