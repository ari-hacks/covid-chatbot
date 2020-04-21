
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [{"name": "Hello"}, {"name": "World"}]

def test_health():
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"message": "Healthy as fuck"}