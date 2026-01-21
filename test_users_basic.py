import requests

def test_get_user_by_id():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status_code == 200

  data = response.json()

  assert data["id"] == 1
  assert "email" in data
  assert isinstance(data["username"], str)
