import telegram
from constants import TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID

def send_audio_to_chat(title, audio, filename, thumb, caption, performer, duration):
    bot = telegram.Bot(token=TELEGRAM_BOT_API_KEY)
    # bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    bot.send_audio(chat_id=TELEGRAM_CHAT_ID, 
        audio=open(audio, 'rb'), 
        thumb=open(thumb, 'rb'),
        title=title,
        caption=caption,
        filename=filename,
        performer=performer,
        duration=duration)
    print("{} irratsaioa bidali da".format(title))