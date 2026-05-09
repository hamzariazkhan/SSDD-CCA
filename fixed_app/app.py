from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

comments = []

@app.route('/')
def home():
    return render_template('login.html')


# ---------------------------
# FIXED SQL INJECTION
# ---------------------------
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # PARAMETERIZED QUERY
    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    if user and check_password_hash(user[2], password):
        return render_template('dashboard.html', username=username)

    return "Invalid Credentials"


# ---------------------------
# FIXED XSS
# ---------------------------
@app.route('/comment', methods=['GET', 'POST'])
def comment():

    global comments

    if request.method == 'POST':
        comment = request.form['comment']

        comments.append(comment)

    return render_template('comment.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)