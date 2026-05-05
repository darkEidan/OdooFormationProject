from domain.models.employee import Employee
from domain.models.enums import EmployeeStatus
from infrastructure.repositories.base_repository import BaseRepository
from infrastructure.queries.employee_queries import EmployeeQueries
class EmployeeRepository(BaseRepository):

    def _map_to_employee(self, row):
        if row is None:
            return None

        return Employee(
            employee_id=row["id"],
            name=row["name"],
            email=row["email"],
            hire_date=row["hire_date"],
            status=EmployeeStatus(row["status"]),
            department_id=row["department_id"],
            role_id=row["role_id"]
        )

    def create_employee(self, employee):

        row = self._execute(EmployeeQueries.INSERT, employee.to_dict(), fetch_one=True)
        return self._map_to_employee(row)

    def get_employee_by_id(self, employee_id):

        row = self._execute(EmployeeQueries.SELECT_BY_ID, {"id": employee_id}, fetch_one=True)
        return self._map_to_employee(row)

    def list_employees(self):

        rows = self._execute(EmployeeQueries.SELECT_ALL, fetch_all=True)
        return [self._map_to_employee(row) for row in rows]

    def get_employee_by_email(self, email):

        row = self._execute(EmployeeQueries.SELECT_BY_EMAIL, {"email": email}, fetch_one=True)
        return self._map_to_employee(row)


