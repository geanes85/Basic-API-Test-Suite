import requests

def test_get_user_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200

  data = response.json()

    assert data["id"] == 1
    assert "email" in data
    assert isinstance(data["username"], str)
    assert isinstance(data, list)
    assert len(data) > 0
    for user in data:
        assert "id" in user
        assert "name" in user
        assert "email" in user
