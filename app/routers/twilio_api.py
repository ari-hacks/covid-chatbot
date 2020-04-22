from fastapi import APIRouter, Request, Response, Body, HTTPException,Header
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from ..models.sms import SmsMessage
from fastapi.responses import PlainTextResponse
import re
from ..services.stats_service import getUsStats,getUkStats

router = APIRouter()

@router.get("/health-check")
async def health():
    return {"Message":'healthy af'}

@router.post("/bot",response_class=PlainTextResponse)
async def bot(request: Request):
    msg = await request.body()
    resp = MessagingResponse()
    resp.message(str(msg))
    msg = str(resp)
    sentMessage = msg[msg.find('Body=')+len('Body='):msg.rfind('&amp;To=')]
    print(sentMessage)
    #based on sent message 
    #return str(sentMessage + u"\U0001F31F")

    #use switch statement 
    if 'uk' in sentMessage:
        return str(getUkStats())
    else:
        return str(sentMessage + u"\U0001F31F")
