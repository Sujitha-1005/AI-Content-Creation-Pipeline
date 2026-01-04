import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
    # Using Llama 3.3 70B - FREE and extremely fast!
    GROQ_MODEL = "llama-3.3-70b-versatile"
    MAX_TOKENS = 4000
    TEMPERATURE = 0.7