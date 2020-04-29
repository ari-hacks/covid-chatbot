from fastapi import APIRouter, Request, Response, Body, HTTPException,Header
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from fastapi.responses import PlainTextResponse
import re
import settings
import httpx
from ..services.stats_service import getUsStats,getUkStats
from ..services.news_service import getNews
router = APIRouter()

@router.get("/health-check")
async def health():
    return {"Message":'healthy news endpoint'}

#route that gets gaurdian good news and randomly selects a link to send after looping through list

@router.get("/theguardian")
async def getGoodNews():
    return getNews()
