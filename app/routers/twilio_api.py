from fastapi import APIRouter, Request, Response, Body, HTTPException,Header
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from fastapi.responses import PlainTextResponse
import re
from ..services.stats_service import getUsStats,getUkStats
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import urllib
import app.chatterbot_custom
import logging

logging.basicConfig(level=logging.INFO)

rona = ChatBot('Rona',
    logic_adapters=[
         {
            "import_path": "chatterbot.logic.BestMatch",
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.65
        } ,
         {
          'import_path':'app.chatterbot_custom.covid_adapter.CustomLogicAdapter',
          'response_selection_method': 'chatterbot.response_selection.get_first_response',
          'statement_comparison_function': 'chatterbot.comparisons.levenshtein_distance'
        },
   
    ],
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

trainer = ChatterBotCorpusTrainer(rona)
trainer.train("chatterbot.corpus.english")
#trainer.export_for_training('data/data_export.json')
#rona.storage.drop()

router = APIRouter()

@router.get("/health-check")
async def health():
    return {"Message":'healthy twilio endpoint'}

@router.post("/bot",response_class=PlainTextResponse)
async def bot(request: Request):
    msg = await request.body()
    resp = MessagingResponse()
    resp.message(str(msg))
    msg = str(resp)
    logging.info(msg)
    sentMessage = msg[msg.find('Body=')+len('Body='):msg.rfind('&amp;To=')]
    parsed_sent_message = urllib.parse.unquote_plus(str(sentMessage))
    logging.info(parsed_sent_message)
    response = rona.get_response(parsed_sent_message)
    return str(str(response))
