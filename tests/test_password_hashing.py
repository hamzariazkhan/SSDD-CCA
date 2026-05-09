import sqlite3

def test_password_hashing():

    conn = sqlite3.connect("../fixed_app/database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username='admin'")

    password = cursor.fetchone()[0]

    conn.close()

    assert password != "admin123"