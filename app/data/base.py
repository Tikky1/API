import sqlite3
import os


DB_PATH=os.getenv("DB_PATH", "app.db")

con=sqlite3.connect(DB_PATH, check_same_thread=False)

con.row_factory=sqlite3.Row

curs=con.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    done INTEGER,
    priority INTEGER
)""")
