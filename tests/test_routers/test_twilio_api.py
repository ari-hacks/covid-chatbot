
from fastapi import FastAPI,Request
from fastapi.testclient import TestClient
from app.main import app
from fastapi.responses import PlainTextResponse

client = TestClient(app)


def test_health():
    response = client.get("/twilio/health-check")
    assert response.status_code == 200
    assert response.json() == {"Message":'healthy twilio endpoint'}


def test_bot():
    response = client.post("/twilio/bot")
    assert response.status_code == 200