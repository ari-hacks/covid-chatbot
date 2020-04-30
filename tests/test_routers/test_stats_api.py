from fastapi import FastAPI,Request
from fastapi.testclient import TestClient
from app.main import app
from fastapi.responses import PlainTextResponse
import requests
import requests_mock
import settings

client = TestClient(app)


def test_health():
    response = client.get("/stats/health-check")
    assert response.status_code == 200
    assert response.json() == {"Message":'healthy stats endpoint'}


def test_getStatsUs(requests_mock):
    payload = [{
    "country": "USA",
    "confirmed": 1066878,
    "recovered": 147473,
    "critical": 18221,
    "deaths": 61797,
    "latitude": 37.09024,
    "longitude": -95.712891
    }]
    
    requests_mock.get(settings.BASE_URL + "/stats/usa", json=payload)
    assert requests.get(settings.BASE_URL + "/stats/usa").status_code == 200
    assert requests.get(settings.BASE_URL + "/stats/usa").json() == payload
    

def test_getStatsUk(requests_mock):
    payload = [{
        "country": "UK",
        "confirmed": 1066878,
        "recovered": 147473,
        "critical": 18221,
        "deaths": 61797,
        "latitude": 37.09024,
        "longitude": -95.712891
        }]
    
    requests_mock.get(settings.BASE_URL + "/stats/uk", json=payload)
    assert requests.get(settings.BASE_URL + "/stats/uk").status_code == 200
    assert requests.get(settings.BASE_URL + "/stats/uk").json() == payload