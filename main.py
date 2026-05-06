from application.services.attendance_service import AttendanceService
from application.services.employee_service import EmployeeService
from application.services.department_service import DepartmentService
from application.services.role_service import RoleService

from api.menu.main_menu import MainMenu


def main():
    employee_service = EmployeeService()
    department_service = DepartmentService()
    role_service = RoleService()
    attendance_service = AttendanceService()

    main_menu = MainMenu(
        employee_service,
        department_service,
        role_service,
        attendance_service
    )

    main_menu.run()


if __name__ == "__main__":
    main()
