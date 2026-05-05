from infrastructure.repositories.base_repository import BaseRepository
from infrastructure.queries.role_queries import RoleQueries
from domain.models.role import Role


class RoleRepository(BaseRepository):

    def _map(self, row):
        if row is None:
            return None
        return Role(row["id"], row["name"], row["level"])

    def create(self, role: Role):
        row = self._execute(RoleQueries.INSERT,{"name": role.name,"level": role.level},fetch_one=True)
        return self._map(row)

    def get_by_id(self, role_id: int):
        row = self._execute(RoleQueries.SELECT_BY_ID,{"id": role_id},fetch_one=True)
        return self._map(row)

    def list(self):
        rows = self._execute(RoleQueries.SELECT_ALL,fetch_all=True)
        return [self._map(r) for r in rows]

    def delete(self, role_id: int):
        self._execute(RoleQueries.DELETE,{"id": role_id})
