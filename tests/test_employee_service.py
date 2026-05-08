import pytest
from application.services.employee_service import EmployeeService
from domain.models.employee import Employee, EmployeeStatus
from datetime import date
from infrastructure.fakes.fake_employee_repository import FakeEmployeeRepo


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
    service = EmployeeService(FakeEmployeeRepo())

    employee = build_employee()
    result = service.create_employee(employee)

    assert result.id is not None


def test_create_employee_duplicate_email():
    service = EmployeeService(FakeEmployeeRepo())

    employee = build_employee()
    service.create_employee(employee)

    with pytest.raises(ValueError):
        service.create_employee(build_employee())


def test_get_employee_success():
    service = EmployeeService(FakeEmployeeRepo())

    employee = service.create_employee(build_employee())

    result = service.get_employee(employee.id)

    assert result.id == employee.id


def test_get_employee_not_found():
    service = EmployeeService(FakeEmployeeRepo())

    with pytest.raises(ValueError):
        service.get_employee(999)


def test_list_employees():
    service = EmployeeService(FakeEmployeeRepo())

    service.create_employee(build_employee())

    result = service.list_employees()

    assert len(result) == 1
