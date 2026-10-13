import os
import base64
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot tokeni
BOT_TOKEN = os.getenv("BOT_TOKEN", "8988147589:AAFSbPOA2tf0yIK95TCWSlInv64jdb3l_Yg")

# Google Gemini API kaliti
_ENC_KEY = "QVEuQWI4Uk42THN2Sk1rRVhsai12czVJeUw4eUl4QkwxWUp3N0JvcGdqZEtBbk9KU05qRWc="
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", base64.b64decode(_ENC_KEY).decode("utf-8"))

# Bot adminining Telegram ID raqami
ADMIN_ID = int(os.getenv("ADMIN_ID", "1855136438"))
