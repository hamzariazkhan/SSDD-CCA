import requests

def test_sql_injection():

    data = {
        "username": "admin' --",
        "password": "anything"
    }

    response = requests.post(
        "http://127.0.0.1:5000/login",
        data=data
    )

    assert "Welcome" not in response.text