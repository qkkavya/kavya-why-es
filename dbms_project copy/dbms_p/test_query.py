from db_config import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT * FROM beneficiaries")

for row in cursor.fetchall():
    print(row)

conn.close()
