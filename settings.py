# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GUARDIAN_ENDPOINT = os.getenv("GUARDIAN_ENDPOINT")
GUARDIAN_KEY = os.getenv("GUARDIAN_KEY")
COVID_STATS_ENDPOINT = os.getenv("COVID_STATS_ENDPOINT")
RAPDIAPI_PROJECT = os.getenv("RAPDIAPI_PROJECT")
X_RAPIDAPI_HOST = os.getenv("X_RAPIDAPI_HOST")
X_RAPIDAPI_KEY = os.getenv("X_RAPIDAPI_KEY")
BASE_URL = os.getenv("BASE_URL")

