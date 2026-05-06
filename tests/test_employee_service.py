import pytest
from application.services.employee_service import EmployeeService
from domain.models.employee import Employee, EmployeeStatus
from datetime import date


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



def build_employee():
    return Employee(
        employee_id=None,
        name="John",
        email="john@test.com",
        hire_date=date.today(),
        status=EmployeeStatus.ACTIVE,
        department_id=1,
        role_id=1
    )


def test_create_employee_success():
    service = EmployeeService()
    service.repo = FakeEmployeeRepo()

    employee = build_employee()
    result = service.create_employee(employee)

    assert result.id is not None


def test_create_employee_duplicate_email():
    service = EmployeeService()
    fake_repo = FakeEmployeeRepo()
    service.repo = fake_repo

    employee = build_employee()
    fake_repo.create_employee(employee)

    with pytest.raises(ValueError):
        service.create_employee(build_employee())


def test_get_employee_success():
    service = EmployeeService()
    fake_repo = FakeEmployeeRepo()
    service.repo = fake_repo

    employee = fake_repo.create_employee(build_employee())

    result = service.get_employee(employee.id)

    assert result.id == employee.id


def test_get_employee_not_found():
    service = EmployeeService()
    service.repo = FakeEmployeeRepo()

    with pytest.raises(ValueError):
        service.get_employee(999)


def test_list_employees():
    service = EmployeeService()
    fake_repo = FakeEmployeeRepo()
    service.repo = fake_repo

    fake_repo.create_employee(build_employee())

    result = service.list_employees()

    assert len(result) == 1
