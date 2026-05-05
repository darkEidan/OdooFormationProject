from infrastructure.database import get_connection
from domain.models.role import Role


class RoleRepository:

    def _map(self, row):
        if not row:
            return None
        return Role(row["id"], row["name"], row["level"])

    def create(self, role: Role):
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO role (name, level)
                    VALUES (%s, %s)
                    RETURNING *;
                """, (role.name, role.level))

                row = cur.fetchone()

            conn.commit()
            return self._map(row)

        except:
            conn.rollback()
            raise

        finally:
            conn.close()
    def get_by_id(self, role_id : int) -> Role | None :
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM role WHERE id = %s;",
                    (role_id,)
                )
                row = cur.fetchone()
                return self._map(row)

        finally:
            conn.close()

    def list(self):
        conn = get_connection()
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM role;")
                return [self._map(r) for r in cur.fetchall()]
        finally:
            conn.close()
