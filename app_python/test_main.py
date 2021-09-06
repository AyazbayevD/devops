import requests

def test_request():
    assert requests.get("http://localhost:5000").status_code == 200