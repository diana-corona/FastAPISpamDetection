from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_spam_detection_query():
	response = client.get("/api/v1/spam_detection_query/?message=winner")
	assert response.status_code == 200
	assert response.json() == {"label":"spam","spam_probability":0.9826203870460608}

