import telegram
from constants import TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID
from audio_compressor import compressAudioUrl

def notify_telegram(message):

    podcast_data = {
        "audio":"./audio/xarmatiropunk-2021-11-16_compressed.mp3",
        "filename":"xarma-tiro-punk-031-asko-falta-da",
        "thumb":"./audio/thumb.jpeg",
        "caption":"Xarma tiro punk #031 Asko falta da?",
        "performer":"xarma tiro punk",
        # "caption": "<img src='http://www.txapairratia.org/wp-content/uploads/2021/11/WhatsApp-Image-2021-11-15-at-23.28.00-1024x739.jpeg' class='webfeedsFeaturedVisual' alt='' /><p>Gaurkuen bixok egon gare uhinen bestaldien, gure &#8220;betiko&#8221; formatuai eutsiz. Txoritxo batek esan dosku gustuko [&#8230;]</p>",
        # "parse_mode":"HTML"
    }


    bot = telegram.Bot(token=TELEGRAM_BOT_API_KEY)
    # bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    bot.send_audio(chat_id=TELEGRAM_CHAT_ID, 
        audio=open(podcast_data["audio"], 'rb'), 
        thumb=open(podcast_data["thumb"], 'rb'), 
        caption=podcast_data["caption"],
        filename=podcast_data["filename"],
        performer=podcast_data["performer"])
    print("Telegram notification sent")
    # import pdb; pdb.set_trace()


if __name__ == '__main__':
    compressAudioUrl("./audio/xarmatiropunk-2021-11-16.mp3", "./audio/compressed/xarmatiropunk-2021-11-16.mp3")
    # notify_telegram('Kaixo mundua')