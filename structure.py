import sqlite3
def init_db():
    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
    create table if not exists users(
        id integer primary key autoincrement,
        username text,
        password text,
        name text,
        is_private text,
        mobile_number text
    )
    """)
        cursor.execute('''
        create table if not exists requests(
        id integer primary key autoincrement,
        requested_by text,
        requested_to text,
        status text,
        is_read text                                      
                       )               
                       ''')
        conn.commit()

