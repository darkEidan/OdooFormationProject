from domain.models.enums import BenefitType, Unit
from domain.models.employee import Employee
from datetime import date


class Benefit:
    def __init__(
        self,
        benefit_id: int,
        name: str,
        benefit_type: BenefitType,
        description: str
    ):
        self.id = benefit_id
        self.name = name
        self.benefit_type = benefit_type
        self.description = description


class EmployeeBenefit:
    def __init__(
        self,
        employee_benefit_id: int,
        employee: Employee,
        benefit: Benefit,
        value: float,
        unit: Unit,
        impact_on_salary: bool,
        start_date: date,
        end_date: date,
        status: str = "active"
    ):
        self.employee_benefit_id = employee_benefit_id
        self.employee = employee
        self.benefit = benefit
        self.value = value
        self.unit = unit
        self.impact_on_salary = impact_on_salary
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    # ===== Business logic =====

    def is_active(self) -> bool:
        if self.status != "active":
            return False
        if self.end_date and self.end_date < date.today():
            return False
        return True

    def compute_value(self, base_salary: float) -> float:
        if self.unit == Unit.PERCENT:
            return base_salary * (self.value / 100)
        return self.value