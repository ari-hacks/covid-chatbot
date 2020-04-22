from fastapi import APIRouter, Request, Response, Body, HTTPException,Header
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from ..models.sms import SmsMessage
from fastapi.responses import PlainTextResponse
import re
import settings
import httpx
from ..services.stats_service import getUsStats,getUkStats

router = APIRouter()

@router.get("/health-check")
async def health():
    return {"Message":'healthy af in stats endpoint'}


@router.get("/usa")
async def getStatsUs():
    return getUsStats()
    
@router.get("/uk")
async def getStatsUk():
    return getUkStats()
