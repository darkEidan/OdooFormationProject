def check_in_cli(service):
    try:
        employee_id = int(input("Employee ID: "))
        attendance = service.check_in(employee_id)
        print("✅ Checked in:", attendance.id)
    except Exception as e:
        print("❌", e)


def check_out_cli(service):
    try:
        employee_id = int(input("Employee ID: "))
        attendance = service.check_out(employee_id)
        print("✅ Checked out:", attendance.id)
    except Exception as e:
        print("❌", e)


def list_attendance_cli(service):
    try:
        employee_id = int(input("Employee ID: "))
        records = service.list_attendance(employee_id)

        if not records:
            print("⚠️ No attendance records found.")
            return

        print("\n📋 Attendance Records:\n")

        for r in records:
            status = "OPEN" if r.is_open() else "CLOSED"
            hours = r.get_worked_hours()

            print(f"""
ID: {r.id}
Check-in : {r.check_in}
Check-out: {r.check_out if r.check_out else '---'}
Status   : {status}
Hours    : {round(hours, 2)}
-------------------------
""")

    except ValueError:
        print("❌ Invalid input")

    except Exception as e:
        print("❌", e)
