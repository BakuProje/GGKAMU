import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "60"))

DEVS = list(map(int, os.getenv("DEVS", "6897960987").split()))

API_ID = int(os.getenv("API_ID", "29119489"))

API_HASH = os.getenv("API_HASH", "85dde49bb0c55b525d4f396d06209dd8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8115675477:AAH37y0bEEVodAvqOvllC8LvWFj1M9tS9r8")

OWNER_ID = int(os.getenv("OWNER_ID", "6897960987"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ubotKuzu:KuzurokenBaku234@bakuzaan.qsum4.mongodb.net/?retryWrites=true&w=majority&appName=bakuzaan")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT"))

USER_GROUP = os.getenv("USER_GROUP", "@testidzkiiih")
