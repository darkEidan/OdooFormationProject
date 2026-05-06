from application.services.employee_service import EmployeeService
from api.cli.employee_cli import create_employee_cli, list_employees_cli, get_employee_cli
from api.menu.base_menu import BaseMenu


class EmployeeMenu(BaseMenu):

    def __init__(self, service: EmployeeService):
        super().__init__("Employee Management")
        self.service = service
        self.configure()

    def configure(self):
        self.options = {
            "1": ("Create employee", lambda: create_employee_cli(self.service)),
            "2": ("Get employee by ID", lambda: get_employee_cli(self.service)),
            "3": ("List employees", lambda: list_employees_cli(self.service)),
            "9": ("Restricted action", self._forbidden)
        }

    def _forbidden(self):
        print("Not allowed at your permission level")
