from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_root_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Welcome to the spam detection API'}

def test_mlpclassifiers():
    response = client.get("/Mlpclassifiers/?message=is this spam")
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_kneighbors():
    response = client.get("/Kneighbors/?message=is this spam")
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_decisiontrees():
    response = client.get("/Decisiontrees/?message=is this spam")
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()

def test_randomforests():
    response = client.get("/Randomforests/?message=is this spam")
    assert response.status_code == 200
    assert 'label' in response.json()
    assert 'spam_probability' in response.json()
    assert 'message' in response.json()