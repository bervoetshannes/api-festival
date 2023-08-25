import requests
import json

headers = {
"accept": "application/json",
"Content-Type": "application/x-www-form-urlencoded"
}

# Account 'test@test.be' with password 'test' has already been pre-made, either manually or with another requests.post
request_data = {
    "client_id": "",
    "client_secret": "",
    "scope": "",
    "grant_type": "",
    "refresh_token": "",
    "username": "test@test.com",
    "password": "test"
}

tokenrequest = requests.post("http://127.0.0.1:8000/token", data=request_data, headers=headers)

# Printing the information for debugging and illustration purposes
print(tokenrequest.text)
# Extracting the token that came with the response
token = json.loads(tokenrequest.text)['access_token']

# Using the token in the headers of a secured endpoint
headerswithtoken = {
"accept" : "application/json",
"Authorization": f'Bearer {token}'
}

getrequest = requests.get("http://localhost:8000/users/me", headers=headerswithtoken)

# Printing the information for debugging and illustration purposes
print(getrequest .text)

create_locatie = {
    "naam": "test",
    "lat": 5.555,
    "lon": 5.555
}

def test_get_locations():
    response = requests.get('http://127.0.0.1:8000/locations/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["naam"] == "test"
    assert response_dictionary["lat"] == 5.555
    assert response_dictionary["lon"] == 5.555

create_user = {
    "email": "test.test@test.com",
}

def test_get_user():
    response = requests.get('http://127.0.0.1:8000/users/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["email"] == "test.test@test.com"

create_festival = {
    "naam": "test",
    "location_id": 1,
    "begin_dat": "1 Jan",
    "end_dat": "2 Jan"
}

def test_get_festival():
    response = requests.get('http://127.0.0.1:8000/festivals/')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert response_dictionary["naam"] == "test"
    assert response_dictionary["location_id"] == 1
    assert response_dictionary["begin_dat"] == "1 Jan"
    assert response_dictionary["end_dat"] == "2 Jan"

