TELEGRAM_BOT_API_KEY = ""
TELEGRAM_CHAT_ID = ""
TXAPA_IRRATIA_RSS_URL = "http://www.txapairratia.org/rss/"

# Katxeak
BIDALITAKO_IRRATSAIOEN_DB = "./db/irratsaio_db.json"
DEFAULT_RSS_LENGTH = "./db/default_rss_length.json"

# Sortu prod_constant.py fitxategia eta gainidatzi nahi dituzun aldagaiak
# Fitxategi hau Git-etik kanpo geratuko da. Beraz, fitxategi hori bakarrik zure makina lokalean izango duzu.
try:
    from prod_constants import *
except ImportError:
    pass
