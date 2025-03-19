import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except:
    
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "gemini-1.5-pro"
MAX_TOKENS = 1000
TEMPERATURE = 0.7

APP_TITLE = "TalentScout Hiring Assistant"
APP_DESCRIPTION = "An AI hiring assistant for TalentScout."

END_KEYWORDS = ["bye", "goodbye", "exit", "quit", "done", "stop"]
