from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import twilio_api,stats_api,news_api

app = FastAPI(
    title="Covid-19 ChatBot",
    description="This is a simple api that gives stats on Covid-19 in the US & UK. The api also provides some good news in light of recent times all transmitted via WhatsApp.",
    version="1.0",
)

app.include_router(twilio_api.router, prefix="/twilio")
app.include_router(stats_api.router, prefix="/stats")
app.include_router(news_api.router, prefix="/news")
