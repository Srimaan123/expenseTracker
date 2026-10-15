import sqlite3
with get_db() as conn:
    cursor = conn.cursor()
    cursor.execute("drop table users")
    print("table deleted successfully")
    conn.commit()