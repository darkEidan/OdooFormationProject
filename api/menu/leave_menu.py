from api.menu.base_menu import BaseMenu
from api.cli.leave_cli import request_leave_cli, approve_leave_cli, reject_leave_cli, list_leaves_cli



class LeaveMenu(BaseMenu):

    def __init__(self, service):
        super().__init__("Leave Management")
        self.service = service
        self.configure()

    def configure(self):
        self.options = {
            "1": ("Request leave", self.request_leave),
            "2": ("Approve leave", self.approve_leave),
            "3": ("Reject leave", self.reject_leave),
            "4": ("List leaves", self.list_leaves),
            "9": ("Restricted action", self._forbidden)
        }

    def request_leave(self):
        request_leave_cli(self.service)

    def approve_leave(self):
        approve_leave_cli(self.service)

    def reject_leave(self):
        reject_leave_cli(self.service)

    def list_leaves(self):
        list_leaves_cli(self.service)

    def _forbidden(self):
        print("Not allowed at your permission level")
