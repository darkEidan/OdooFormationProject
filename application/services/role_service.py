from infrastructure.repositories.role_repository import RoleRepository
from domain.models.role import Role

class RoleService:

    def __init__(self, role_repo : RoleRepository):
        self.repo = role_repo

    def create(self, name, level):
        return self.repo.create(Role(None, name, level))

    def list(self):
        return self.repo.list()

    def get_by_id(self, role_id : int ) -> Role | None:
        return  self.repo.get_by_id(role_id)