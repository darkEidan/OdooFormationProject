from api.cli.role_cli import create_role_cli, list_roles_cli
from api.menu.base_menu import BaseMenu


class RoleMenu(BaseMenu):

    def __init__(self, service):
        super().__init__("Role Management")
        self.service = service
        self.configure()

    def configure(self):
        self.options = {
            "1": ("Create role", lambda: create_role_cli(self.service)),
            "2": ("List roles", lambda: list_roles_cli(self.service)),
            "9": ("Restricted action", self._forbidden)
        }

    def _forbidden(self):
        print("Not allowed at your permission level")
