from infrastructure.database import get_connection

class EmployeeRepository:

    def create_employee(self, name, email, hire_date, status, department_id, role_id):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO employee (name, email, hire_date, status, department_id, role_id)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    RETURNING *;
                """, (name, email, hire_date, status, department_id, role_id))

                result = cur.fetchone()

            conn.commit()
            return result

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()

    def get_employee_by_id(self, employee_id):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM employee WHERE id = %s;", (employee_id,))
                return cur.fetchone()

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


