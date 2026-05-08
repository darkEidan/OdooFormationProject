class FakeEmployeeRepo:

    def __init__(self):
        self.employees = []
        self.next_id = 1

    def create_employee(self, employee):
        employee.id = self.next_id
        self.next_id += 1
        self.employees.append(employee)
        return employee

    def get_employee_by_id(self, employee_id):
        for e in self.employees:
            if e.id == employee_id:
                return e
        return None

    def get_employee_by_email(self, email):
        for e in self.employees:
            if e.email == email:
                return e
        return None

    def list_employees(self):
        return self.employees