import sqlite3
def init_db():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
    create table if not exists users(
        id integer primary key autoincrement,
        username text,
        password text,
        mobile_number text
    )
    """)
        conn.commit()

