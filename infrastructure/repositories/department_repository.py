from infrastructure.repositories.base_repository import BaseRepository
from infrastructure.queries.department_queries import DepartmentQueries
from domain.models.department import Department


class DepartmentRepository(BaseRepository):

    def _map(self, row):
        if row is None:
            return None
        return Department(row["id"], row["name"])

    def create(self, department: Department):
        row = self._execute(DepartmentQueries.INSERT,{"name": department.name},fetch_one=True)
        return self._map(row)

    def get_by_id(self, department_id: int):
        row = self._execute(DepartmentQueries.SELECT_BY_ID,{"id": department_id}, fetch_one=True )
        return self._map(row)

    def list(self):
        rows = self._execute(DepartmentQueries.SELECT_ALL, fetch_all=True)
        return [self._map(r) for r in rows]

    def delete(self, department_id: int):
        self._execute(DepartmentQueries.DELETE,{"id": department_id})
