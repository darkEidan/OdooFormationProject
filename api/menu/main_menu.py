from api.menu.base_menu import BaseMenu
from api.menu.employee_menu import EmployeeMenu
from api.menu.department_menu import DepartmentMenu
from api.menu.role_menu import RoleMenu
from api.menu.attendance_menu import AttendanceMenu

class MainMenu(BaseMenu):

    def __init__(self, employee_service, department_service, role_service, attendance_service):
        super().__init__("Main Menu")

        self.employee_menu = EmployeeMenu(employee_service)
        self.department_menu = DepartmentMenu(department_service)
        self.role_menu = RoleMenu(role_service)
        self.attendance_menu = AttendanceMenu(attendance_service)

        self.configure()

    def configure(self):
        self.options = {
            "1": ("Employee Management", self.open_employee_menu),
            "2": ("Department Management", self.open_department_menu),
            "3": ("Role Management", self.open_role_menu),
            "4": ("Attendance", self.open_attendance_menu)
        }

    def open_employee_menu(self):
        self.employee_menu.run()

    def open_department_menu(self):
        self.department_menu.run()

    def open_role_menu(self):
        self.role_menu.run()

    def open_attendance_menu(self):
        self.attendance_menu.run()