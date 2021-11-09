from fastapi.testclient import TestClient
from unittest.mock import patch

from pwd_functions import get_password_hash
from login_functions import  get_current_active_user
from pwd_functions import verify_password

from main import app

client = TestClient(app)

async def override_current_active_user():
    return { 'user_id': 1, 'username': 'johndoe', 'hashed_password': get_password_hash('secret'), 'email': 'johndoe@johndoe.com', 'full_name': 'johndo' }

app.dependency_overrides[get_current_active_user] = override_current_active_user

def test_root_main():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() 

def test_mlpclassifiers():
    response = client.get('/Mlpclassifiers/?message=is this spam')
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_kneighbors():
    response = client.get('/Kneighbors/?message=is this spam')
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_decisiontrees():
    response = client.get('/Decisiontrees/?message=is this spam')
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_randomforests():
    response = client.get('/Randomforests/?message=is this spam')
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_current_user():
    response = client.get('/users/me')
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['user_id'] == 1
    assert json_response['username'] == 'johndoe'
    assert json_response['email'] == 'johndoe@johndoe.com'
    assert json_response['full_name'] == 'johndo'
    assert verify_password('secret',json_response['hashed_password'])
