from api.cli.department_cli import create_department_cli, list_departments_cli
from api.menu.base_menu import BaseMenu


class DepartmentMenu(BaseMenu):

    def __init__(self, service):
        super().__init__("Department Management")
        self.service = service
        self.configure()

    def configure(self):
        self.options = {
            "1": ("Create department", lambda: create_department_cli(self.service)),
            "2": ("List departments", lambda: list_departments_cli(self.service)),
            "9": ("Delete department", self._forbidden)
        }

    def _forbidden(self):
        print("Not allowed at your permission level")
