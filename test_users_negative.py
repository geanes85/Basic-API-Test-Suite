import requests

def test_get_non_existent_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/9999")  # ___
    assert response.status_code == 404
    data = response.json()
    assert data == {}
