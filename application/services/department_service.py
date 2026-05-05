from infrastructure.repositories.department_repository import DepartmentRepository
from domain.models.department import Department


class DepartmentService:

    def __init__(self):
        self.repo = DepartmentRepository()

    def create(self, name):
        return self.repo.create(Department(None, name))

    def get_by_id(self, department_id : int)-> Department | None :
        return self.repo.get_by_id(department_id)

    def list(self):
        return self.repo.list()