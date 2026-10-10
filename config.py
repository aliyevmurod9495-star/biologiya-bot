import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot tokeni
BOT_TOKEN = os.getenv("BOT_TOKEN", "8988147589:AAFSbPOA2tf0yIK95TCWSlInv64jdb3l_Yg")

# Bot adminining Telegram ID raqami
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
