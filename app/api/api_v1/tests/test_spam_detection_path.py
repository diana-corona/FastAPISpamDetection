from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_spam_detection_path():
	response = client.get("/api/v1/spam_detection_path/hi")
	assert response.status_code == 200
	assert response.json() == {"label":"ham","spam_probability":5.450550601570071e-06}

