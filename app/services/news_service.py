import httpx
import settings


def getUsStats():
    headers = {'x-rapidapi-host': settings.X_RAPIDAPI_HOST,
               'x-rapidapi-key': settings.X_RAPIDAPI_KEY, 'accept': 'application/json'}
    response =  httpx.get(settings.COVID_STATS_ENDPOINT + '?format=json&name=usa', headers=headers)
    return response.json()
   
   
