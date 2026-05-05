from infrastructure.database import get_connection
from domain.models.employee import Employee
from domain.models.enums import EmployeeStatus

class EmployeeRepository:

    def _map_to_employee(self, row):
        if row is None:
            return None

        return Employee(
            employee_id=row["id"],
            name=row["name"],
            email=row["email"],
            hire_date=row["hire_date"],
            status=EmployeeStatus(row["status"]),
            department_id=row["department_id"],
            role_id=row["role_id"]
        )


    def create_employee(self, employee : Employee):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO employee (name, email, hire_date, status, department_id, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING *;
                """, (
                    employee.name,
                    employee.email,
                    employee.hire_date,
                    employee.status.value,
                    employee.department_id,
                    employee.role_id
                ))

                row = cur.fetchone()

            conn.commit()
            return self._map_to_employee(row)

        except:
            conn.rollback()
            raise

        finally:
            conn.close()

    def get_employee_by_id(self, employee_id):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM employee WHERE id = %s;",
                    (employee_id,)
                )
                row = cur.fetchone()
                return self._map_to_employee(row)

        finally:
            conn.close()

    def list_employees(self):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employee;")
                return cur.fetchall()

        finally:
            conn.close()

    def get_employee_by_email(self, email):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employee WHERE email = %s;", (email,))
                return cur.fetchone()
        finally:
            conn.close()


