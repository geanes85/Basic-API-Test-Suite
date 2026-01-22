import requests

def test_user_response_time():
    response = requests.___("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    response_time = response.elapsed.total_seconds()
    assert response_time < 0.5
