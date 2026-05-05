from infrastructure.database import get_connection


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

