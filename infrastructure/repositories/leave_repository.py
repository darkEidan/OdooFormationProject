from infrastructure.repositories.base_repository import BaseRepository
from infrastructure.queries.leave_queries import LeaveQueries
from domain.models.leave import Leave
from domain.models.enums import LeaveStatus, LeaveType


class LeaveRepository(BaseRepository):

    def _map(self, row):
        if row is None:
            return None

        leave = Leave(
            id=row["id"],
            employee_id=row["employee_id"],
            start_date=row["start_date"],
            end_date=row["end_date"],
            leave_type=LeaveType(row["leave_type"]),
            status=LeaveStatus(row["status"])
        )

        leave.created_at = row["created_at"]

        return leave

    def create(self, leave: Leave):
        row = self._execute(
            LeaveQueries.INSERT,
            {
                "employee_id": leave.employee_id,
                "leave_type": leave.leave_type.value,
                "start_date": leave.start_date,
                "end_date": leave.end_date,
                "status": leave.status.value
            },
            fetch_one=True
        )
        return self._map(row)

    def get_by_id(self, leave_id: int):
        row = self._execute(
            LeaveQueries.SELECT_BY_ID,
            {"id": leave_id},
            fetch_one=True
        )
        return self._map(row)

    def list_by_employee(self, employee_id: int):
        rows = self._execute(
            LeaveQueries.SELECT_BY_EMPLOYEE,
            {"employee_id": employee_id},
            fetch_all=True
        )
        return [self._map(r) for r in rows]

    def update(self, leave: Leave):
        row = self._execute(
            LeaveQueries.UPDATE,
            {
                "id": leave.id,
                "employee_id": leave.employee_id,
                "leave_type": leave.leave_type.value,
                "start_date": leave.start_date,
                "end_date": leave.end_date,
                "status": leave.status.value,
            },
            fetch_one=True
        )
        return self._map(row)

    def delete(self, leave_id: int):
        self._execute(
            LeaveQueries.DELETE,
            {"id": leave_id}
        )

    def find_overlapping(self, employee_id: int, start_date, end_date):
        rows = self._execute(
            LeaveQueries.SELECT_OVERLAPPING,
            {
                "employee_id": employee_id,
                "start_date": start_date,
                "end_date": end_date
            },
            fetch_all=True
        )
        return [self._map(r) for r in rows]

