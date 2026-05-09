import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

cursor.execute("DELETE FROM users")

hashed_password = generate_password_hash("admin123")

cursor.execute("""
INSERT INTO users(username,password)
VALUES(?,?)
""", ("admin", hashed_password))

conn.commit()
conn.close()

print("Secure database initialized.")