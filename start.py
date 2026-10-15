import sqlitecloud
from contextlib import contextmanager
import sqlite3
CONNECTION_STRING = "sqlitecloud://cnbbdsijvz.g5.sqlite.cloud:8800/data.sqlite?apikey=aMfhZscsynnklnSIJT40biQMD6NDns3wWqH5OOF6TvM"

@contextmanager
def get_db():
    conn = None
    is_cloud = False
    
    # Try reaching out to SQLite Cloud first if the string exists
    if CONNECTION_STRING:
        try:
            import sqlitecloud
            # Keep a tight 3-second timeout so it fails fast inside Kasm
            conn = sqlitecloud.connect(CONNECTION_STRING, timeout=3.0)
            is_cloud = True
            print("☁️ Connected to SQLite Cloud successfully!")
        except Exception as e:
            print(f"⚠️ Cloud connection failed ({e}). Falling back to local offline mode...")
            conn = None
            
    # If the cloud failed or no connection string was provided, fall back locally
    if conn is None:
        conn = sqlite3.connect("local_tracker.db")
        print("💾 Running on local offline database (local_tracker.db).")

    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()