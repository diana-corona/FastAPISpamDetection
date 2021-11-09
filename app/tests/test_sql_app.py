from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as _sql

from ..database import Base
from ..main import app
from ..db_functions import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./testdatabase.db"
engine = _sql.create_engine(
	SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user():
    response = client.post(
        "/users/",
        json={ "user_id": 1, "username": "johndoe", "password": "secret", "email": "johndoe@johndoe.com", "full_name": "johndo" }
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "johndoe@johndoe.com"
    assert "user_id" in data

def test_create_duplicate_user():
    response = client.post(
        "/users/",
        json={ "user_id": 1, "username": "johndoe", "password": "secret", "email": "johndoe@johndoe.com", "full_name": "johndo" }
    )
    assert response.status_code == 400, response.text
