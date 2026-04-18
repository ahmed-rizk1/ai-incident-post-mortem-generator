import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    API_PORT = int(os.getenv("API_PORT", 8000))

config = Config()
