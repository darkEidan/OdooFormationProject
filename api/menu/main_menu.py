from api.menu.base_menu import BaseMenu
from api.menu.employee_menu import EmployeeMenu
from api.menu.department_menu import DepartmentMenu
from api.menu.role_menu import RoleMenu
from api.menu.attendance_menu import AttendanceMenu
from api.menu.leave_menu import LeaveMenu
from application.services.container import Container

class MainMenu(BaseMenu):

    def __init__(self, main_service : Container):
        super().__init__("Main Menu")

        self.employee_menu = EmployeeMenu(main_service.employee_service)
        self.department_menu = DepartmentMenu(main_service.department_service)
        self.role_menu = RoleMenu(main_service.role_service)
        self.attendance_menu = AttendanceMenu(main_service.attendance_service)
        self.leave_menu = LeaveMenu(main_service.leave_service)

        self.configure()

    def configure(self):
        self.options = {
            "1": ("Employee Management", self.open_employee_menu),
            "2": ("Department Management", self.open_department_menu),
            "3": ("Role Management", self.open_role_menu),
            "4": ("Attendance", self.open_attendance_menu),
            "5": ("Leave Management", self.open_leave_menu)
        }

    def open_employee_menu(self):
        self.employee_menu.run()

    def open_department_menu(self):
        self.department_menu.run()

    def open_role_menu(self):
        self.role_menu.run()

    def open_attendance_menu(self):
        self.attendance_menu.run()

    def open_leave_menu(self):
        self.leave_menu.run()