import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set")

MODEL_NAME = "gemini-1.5-pro"
MAX_TOKENS = 1000
TEMPERATURE = 0.7

APP_TITLE = "TalentScout Hiring Assistant"
APP_DESCRIPTION = "An AI hiring assistant for TalentScout."

END_KEYWORDS = ["bye", "goodbye", "exit", "quit", "done", "stop"]
