import os

API_ID    = os.environ.get("API_ID", "28771159")
API_HASH  = os.environ.get("API_HASH", "a6ff05d5e26feb62d29eea1c411a15b9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
