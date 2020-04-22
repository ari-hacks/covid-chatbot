from pydantic import BaseModel
from typing import List, Optional

class SmsMessage(BaseModel):
    sms: str


class UkStats(BaseModel):
    sms: str



class UsStats(BaseModel):
    sms: str



