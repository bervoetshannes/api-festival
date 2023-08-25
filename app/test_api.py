import requests
import json


create_locatie = {
    "naam": "test",
    "lat": 5.555,
    "lon": 5.555
}

def test_get_locations():
    response = requests.get('http://127.0.0.1:8000/locations/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
