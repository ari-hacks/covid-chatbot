import httpx
import settings
import logging
import random 

# TODO: 
# replace guardian api with positive coronavirus related tweets 
# 
logging.basicConfig(level=logging.INFO)

def getNews():
    results = []
    url = []
    params = {
         'order-by': "relevance",
         'show-fields': 'webTitle,webUrl',
         'page-size': 10,
         'from-date':'2020-03-20',
         'api-key': settings.GUARDIAN_KEY
    }
    response = httpx.get(settings.GUARDIAN_ENDPOINT, params=params)
    res = response.json()
    results.extend(res['response']['results'])
    for r in results:
        url.append(r['webUrl'])
    return random.choice(url)

