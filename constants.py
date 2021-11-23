TELEGRAM_BOT_API_KEY = ""
TELEGRAM_CHAT_ID = ""
TXAPA_IRRATIA_RSS_URL = "http://www.txapairratia.org/rss/"


# Zenbatero exekutatu beharko da rss-a eskatzeko ataza?
RSS_CHECKER_TASK_IN_MINUTES = 10

# Katxeak
BIDALITAKO_IRRATSAIOEN_DB = "./db/irratsaio_db.json"
DEFAULT_RSS_LENGTH = "./db/default_rss_length.json"

# Sortu prod_constant.py fitxategia eta gainidatzi nahi dituzun aldagaiak
# Fitxategi hau Git-etik kanpo geratzen da. Beraz, bakarrik zure makina lokalean geratuko da.
try:
    from prod_constants import *
except ImportError:
    pass
