from infrastructure.database import get_connection


# def create_employee(data):
#     conn = get_connection()
#
#     try:
#         with conn.cursor() as cur:
#             cur.execute("""
#                         INSERT INTO employee (name, email, hire_date, status, department_id, role_id)
#                         VALUES (%s, %s, %s, %s, %s, %s)
#                         """, data)
#
#         conn.commit()
#
#     except Exception:
#         conn.rollback()
#         raise
#
#     finally:
#         conn.close()

conn = get_connection()
try:

    with conn.cursor() as cur:
        cur.execute("SELECT * FROM employee LIMIT 3;")
        result = cur.fetchall()

    print("Employees:", result)

    print("✅ Connection OK:", result)

except Exception as e:
    print("❌ Connection failed:", e)

finally:
    if 'conn' in locals():
        conn.close()

