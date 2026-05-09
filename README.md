# Secure Login Project

## Features
- Vulnerable Login System
- Fixed Secure Login System
- SQL Injection Demo
- XSS Demo
- Password Hashing Demo
- Automated Security Tests

---

# Setup

## Install Dependencies

cd vulnerable_app

pip install -r requirements.txt

---

# Initialize Database

python init_db.py

---

# Run Vulnerable App

python app.py

---

# Run Fixed App

cd fixed_app

python init_db.py

python app.py

---

# Run Tests

pytest tests/

---

# Vulnerabilities

## 1. SQL Injection
Attack:
admin' --

Fix:
Parameterized queries

---

## 2. Cross-Site Scripting (XSS)
Attack:
<script>alert('xss')</script>

Fix:
Output escaping

---

## 3. Weak Password Storage
Attack:
Passwords visible in database

Fix:
Password hashing using Werkzeug
