import os

API_ID    = os.environ.get("API_ID", "25364269")
API_HASH  = os.environ.get("API_HASH", "ddfbbd94cf441e22ee71bb7f4695c2f1")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
