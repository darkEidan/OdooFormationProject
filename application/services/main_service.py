from application.services.attendance_service import AttendanceService
from application.services.employee_service import EmployeeService
from application.services.department_service import DepartmentService
from application.services.role_service import RoleService
from application.services.leave_service import LeaveService

class MainService :

    def __init__(self):
        self.employee_service = EmployeeService()
        self.department_service = DepartmentService()
        self.role_service = RoleService()
        self.attendance_service = AttendanceService()
        self.leave_service = LeaveService()