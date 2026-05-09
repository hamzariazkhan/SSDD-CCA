from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

comments = []

@app.route('/')
def home():
    return render_template('login.html')


# ---------------------------
# SQL INJECTION VULNERABILITY
# ---------------------------
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # VULNERABLE QUERY
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)

    user = cursor.fetchone()

    conn.close()

    if user:
        return render_template('dashboard.html', username=username)

    return "Invalid Credentials"


# ---------------------------
# XSS VULNERABILITY
# ---------------------------
@app.route('/comment', methods=['GET', 'POST'])
def comment():

    global comments

    if request.method == 'POST':
        comment = request.form['comment']

        # UNSAFE STORAGE
        comments.append(comment)

    return render_template('comment.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)