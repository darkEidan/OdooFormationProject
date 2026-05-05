from infrastructure.database import get_connection


class BaseRepository:

    def _execute(self, query: str, params=None, fetch_one=False, fetch_all=False):
        conn = get_connection()

        try:
            with conn.cursor() as cur:
                cur.execute(query, params or {})

                if fetch_one:
                    result = cur.fetchone()
                elif fetch_all:
                    result = cur.fetchall()
                else:
                    result = None

            conn.commit()
            return result

        except Exception:
            conn.rollback()
            raise

        finally:
            conn.close()
