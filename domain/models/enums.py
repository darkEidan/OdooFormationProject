from enum import Enum

class EmployeeStatus(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    TERMINATED = "terminated"


class LeaveStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class BenefitType(Enum):
    FIXED = "fixed"
    PERCENTAGE = "percentage"
    IN_KIND = "in_kind"


class Unit(Enum):
    EUR = "eur"
    PERCENT = "percent"

class LeaveType(Enum):
    PAID = "paid"
    SICK = "sick"
    UNPAID = "unpaid"