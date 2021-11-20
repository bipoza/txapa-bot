import telegram
from constants import TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID

def notify_telegram(message):

    bot = telegram.Bot(token=TELEGRAM_BOT_API_KEY)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)



if __name__ == '__main__':
    notify_telegram('Kaixo mundua')