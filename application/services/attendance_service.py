from datetime import datetime
from infrastructure.protocols.attendance_repository_protocol import AttendanceRepositoryProtocol


class AttendanceService:

    def __init__(self, attendance_repo : AttendanceRepositoryProtocol):
        self.repo = attendance_repo

    def check_in(self, employee_id):
        existing = self.repo.get_open_attendance(employee_id)

        if existing:
            raise ValueError(f"Already checked in at {existing.check_in}. Please check out first.")

        return self.repo.check_in(employee_id, datetime.now())

    def check_out(self, employee_id):
        existing = self.repo.get_open_attendance(employee_id)

        if not existing:
            raise ValueError("No active check-in found")

        return self.repo.check_out(employee_id, datetime.now())

    def list_attendance(self, employee_id):
        return self.repo.list_by_employee(employee_id)
