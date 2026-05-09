import requests

def test_xss():

    payload = "<script>alert('xss')</script>"

    requests.post(
        "http://127.0.0.1:5000/comment",
        data={"comment": payload}
    )

    response = requests.get(
        "http://127.0.0.1:5000/comment"
    )

    assert payload not in response.text