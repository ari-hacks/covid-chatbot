from pydantic import BaseModel
from typing import List, Optional


class UsaStatistics():
      country: str
      confirmed: int
      recovered: int 
      critical: int 
      deaths: int 

class UkStatistics():
      country: str
      confirmed: int
      recovered: int 
      critical: int 
      deaths: int 

class GuardianNews():
     url: str