import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # from .env
if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN not set. Copy .env.example -> .env and fill BOT_TOKEN")
# ... remainder of your EduBot code ...
