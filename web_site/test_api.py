import pytest
from app import client


def test_index():
    response = client.get('/news')
    assert response.status_code == 200
    
def test_login():
    response = client.get('/log')
    assert response.status_code == 200

def test_valid_auth():
    data={"login": "vvn",
          "password" : "user"}
    response = client.post('/log', data=data)
    assert response.status_code == 302

def test_invalid_auth():
    data={"login": "vvn",
          "password" : "cisco"}
    response = client.post('/auth/login', data=data)
    assert response.status_code == 200
