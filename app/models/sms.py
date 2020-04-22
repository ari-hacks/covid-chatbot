from pydantic import BaseModel
from typing import List, Optional

class SmsMessage(BaseModel):
    sms: str
