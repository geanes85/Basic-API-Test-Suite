import requests

def test_user_schema():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    required_keys = ["id", "name", "username", "email", "address", "phone", "website"]
    for key in required_keys:
        assert key in data
