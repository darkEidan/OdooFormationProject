from typing import Protocol


class AttendanceRepositoryProtocol(Protocol):

    def check_in(self, employee_id, check_in):
        ...

    def check_out(self, employee_id, check_out):
        ...

    def get_open_attendance(self, employee_id):
        ...

    def list_by_employee(self, employee_id):
        ...
