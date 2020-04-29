
from fastapi import FastAPI,Request
from fastapi.testclient import TestClient
from app.main import app
from fastapi.responses import PlainTextResponse
#refractor api test per route 
client = TestClient(app)


def test_health():
    response = client.get("/stats/health-check")
    assert response.status_code == 200
    assert response.json() == {"Message":'healthy stats endpoint'}


# def test_bot():
#     data = ''
#     response = client.post("/bot",data=data)
#     assert response.status_code == 200
#     assert response.content == data 