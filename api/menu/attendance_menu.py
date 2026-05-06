from api.menu.base_menu import BaseMenu
from api.cli.attendance_cli import check_in_cli,check_out_cli,list_attendance_cli


class AttendanceMenu(BaseMenu):

    def __init__(self, service):
        super().__init__("Attendance Management")
        self.service = service
        self.configure()

    def configure(self):
        self.options = {
            "1": ("Check-in", self.check_in),
            "2": ("Check-out", self.check_out),
            "3": ("List attendance", self.list_attendance),
            "9": ("Restricted action", self._forbidden)
        }

    def check_in(self):
        check_in_cli(self.service)

    def check_out(self):
        check_out_cli(self.service)

    def list_attendance(self):
        list_attendance_cli(self.service)

    def _forbidden(self):
        print("Not allowed at your permission level")
