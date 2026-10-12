import sqlite3
with sqlite3.connect("data.db") as conn:
    cursor = conn.cursor()
    cursor.execute("drop table users")
    print("table deleted successfully")
    conn.commit()