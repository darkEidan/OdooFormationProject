from infrastructure.repositories.leave_repository import LeaveRepository
from infrastructure.repositories.employee_repository import EmployeeRepository
from infrastructure.repositories.department_repository import DepartmentRepository
from infrastructure.repositories.role_repository import RoleRepository
from infrastructure.repositories.attendance_repository import AttendanceRepository

from application.services.leave_service import LeaveService
from application.services.employee_service import EmployeeService
from application.services.department_service import DepartmentService
from application.services.role_service import RoleService
from application.services.attendance_service import AttendanceService

#Container for Repo and Services, no logic inside !
class Container:

    def __init__(self):
        # Repositories
        self.leave_repository = LeaveRepository()
        self.employee_repository = EmployeeRepository()
        self.department_repository = DepartmentRepository()
        self.role_repository = RoleRepository()
        self.attendance_repository = AttendanceRepository()

        # Services with dependencies injections.
        self.leave_service = LeaveService(self.leave_repository)
        self.employee_service = EmployeeService(self.employee_repository)
        self.department_service = DepartmentService(self.department_repository)
        self.role_service = RoleService(self.role_repository)
        self.attendance_service = AttendanceService(self.attendance_repository)