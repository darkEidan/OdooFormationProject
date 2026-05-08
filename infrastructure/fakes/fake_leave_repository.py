from domain.models.leave import Leave


class FakeLeaveRepo:

    def __init__(self):
        self.leaves = []
        self.next_id = 1

    def create(self, leave: Leave) -> Leave:
        leave.id = self.next_id
        self.next_id += 1

        self.leaves.append(leave)

        return leave

    def get_by_id(self, leave_id: int) -> Leave | None:
        for leave in self.leaves:
            if leave.id == leave_id:
                return leave

        return None

    def list_by_employee(self, employee_id: int) -> list[Leave]:
        return [
            leave
            for leave in self.leaves
            if leave.employee_id == employee_id
        ]

    def update(self, leave: Leave) -> Leave | None:
        for index, existing_leave in enumerate(self.leaves):

            if existing_leave.id == leave.id:
                self.leaves[index] = leave
                return leave

        return None

    def delete(self, leave_id: int) -> None:
        self.leaves = [
            leave
            for leave in self.leaves
            if leave.id != leave_id
        ]

    def find_overlapping(self, employee_id, start_date, end_date):
        return [
            leave
            for leave in self.leaves
            if leave.employee_id == employee_id
            and not (
                leave.end_date < start_date
                or leave.start_date > end_date
            )
        ]
