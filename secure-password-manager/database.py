import sqlite3
from pathlib import Path

DB_PATH = Path("data/passwords.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        website TEXT,
        username TEXT,
        password TEXT,
        notes TEXT
    )
    """)
    conn.commit()
    conn.close()
