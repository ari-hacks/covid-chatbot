from fastapi import Depends, FastAPI, Header, HTTPException

from .routers import twilio_api,stats_api

app = FastAPI()

app.include_router(twilio_api.router, prefix="/twilio")
app.include_router(stats_api.router, prefix="/stats")