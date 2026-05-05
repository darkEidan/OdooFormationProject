from infrastructure.database import get_connection
from domain.models.department import Department


class DepartmentRepository:

    def _map(self, row):
        if not row:
            return None
        return Department(row["id"], row["name"])

    def create(self, department: Department):
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO department (name)
                    VALUES (%s)
                    RETURNING *;
                """, (department.name,))
                row = cur.fetchone()

            conn.commit()
            return self._map(row)

        except:
            conn.rollback()
            raise

        finally:
            conn.close()

    def get_by_id(self, department_id : int) -> Department | None :
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM department WHERE id = %s;",
                    (department_id,)
                )
                row = cur.fetchone()
                return self._map(row)

        finally:
            conn.close()

    def list(self):
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM department;")
                return [self._map(r) for r in cur.fetchall()]
        finally:
            conn.close()
