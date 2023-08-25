import requests
import json

def test_get_locations():
    response = requests.get('http://127.0.0.1:8000/locations/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
