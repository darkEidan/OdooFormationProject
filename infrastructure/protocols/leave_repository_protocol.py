from typing import Protocol
from domain.models.leave import Leave


class LeaveRepositoryProtocol(Protocol):


    def create(self, leave: Leave):
        ...

    def get_by_id(self, leave_id: int):
        ...

    def list_by_employee(self, employee_id: int):
        ...

    def update(self, leave: Leave):
        ...

    def delete(self, leave_id: int):
        ...

    def find_overlapping(self,employee_id: int,start_date,end_date) -> list[Leave]:
        ...

