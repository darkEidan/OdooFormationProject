from datetime import datetime
from domain.models.leave import Leave
from domain.models.enums import LeaveType


def request_leave_cli(service):
    try:
        employee_id = int(input("Employee ID: "))
        start = datetime.strptime(input("Start date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        end = datetime.strptime(input("End date (YYYY-MM-DD): "), "%Y-%m-%d").date()

        print("1. Paid\n2. Sick\n3. Unpaid")
        choice = input("Leave type: ")

        leave_type = {
            "1": LeaveType.PAID,
            "2": LeaveType.SICK,
            "3": LeaveType.UNPAID
        }.get(choice)

        if not leave_type:
            print("❌ Invalid leave type")
            return

        leave = Leave(
            id=None,
            employee_id=employee_id,
            start_date=start,
            end_date=end,
            leave_type=leave_type
        )

        result = service.request_leave(leave)

        print(f"✅ Leave requested with ID: {result.id}")

    except ValueError as e:
        print("❌", e)
    except Exception as e:
        print("❌ Unexpected error:", e)


def approve_leave_cli(service):
    try:
        leave_id = int(input("Leave ID: "))
        leave = service.approve_leave(leave_id)
        print(f"✅ Leave {leave.id} approved")
    except Exception as e:
        print("❌", e)


def reject_leave_cli(service):
    try:
        leave_id = int(input("Leave ID: "))
        leave = service.reject_leave(leave_id)
        print(f"❌ Leave {leave.id} rejected")
    except Exception as e:
        print("❌", e)


def list_leaves_cli(service):
    try:
        employee_id = int(input("Employee ID: "))
        leaves = service.list_employee_leaves(employee_id)

        if not leaves:
            print("⚠️ No leaves found")
            return

        for l in leaves:
            print(f"""
                    ID: {l.id}
                    Type: {l.leave_type.value}
                    Start: {l.start_date}
                    End: {l.end_date}
                    Status: {l.status.value}
                    Duration: {l.duration()} days
                    -------------------------
                    """)

    except Exception as e:
        print("❌", e)
