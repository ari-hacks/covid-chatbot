from fastapi import APIRouter, Request, Response, Body, HTTPException,Header
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from ..models.sms import SmsMessage
from fastapi.responses import PlainTextResponse
import re


router = APIRouter()
resp = MessagingResponse()
msg = resp.message()


@router.get("/")
async def read():
    return [{"name": "Hello"}, {"name": "World"}]


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
    return str(sentMessage)
