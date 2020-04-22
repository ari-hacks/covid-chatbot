
from fastapi import FastAPI,Request
from fastapi.testclient import TestClient
from app.main import app
from fastapi.responses import PlainTextResponse

client = TestClient(app)

def test_read():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [{"name": "Hello"}, {"name": "World"}]

def test_health():
    response = client.get("/health-check")
    assert response.status_code == 200
    assert response.json() == {"Message":'healthy af'}


# def test_bot():
#     data = ''
#     response = client.post("/bot",data=data)
#     assert response.status_code == 200
#     assert response.content == data 