
from fastapi import FastAPI,Request
from fastapi.testclient import TestClient
from app.main import app
from fastapi.responses import PlainTextResponse
import requests
import requests_mock
import settings


client = TestClient(app)


def test_health():
    response = client.get("/news/health-check")
    assert response.status_code == 200
    assert response.json() ==  {"Message":'healthy news endpoint'}


def test_bot(requests_mock):
    #fix payload formatting issue
    #payload ='https://www.theguardian.com/world/2020/apr/03/ploughing-through-coronavirus-news-for-the-brighter-stories'
    
    requests_mock.get(settings.BASE_URL + "/news/theguardian")
    assert requests.get(settings.BASE_URL + "/news/theguardian").status_code == 200
    #assert requests.get(settings.BASE_URL + "/news/theguardian") == payload