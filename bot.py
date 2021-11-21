import telegram
from constants import TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID
from audio_compressor import compress_audio_url
from get_rss import get_news_items, get_rss_items_in_json_from_file, save_rss_items_in_json_to_file
from utils import download_from_url



def save_item_to_file(item):
    json_db = get_rss_items_in_json_from_file()
    json_db.append(item)
    save_rss_items_in_json_to_file(json_db)

def notify_telegram(audio, filename, thumb, caption, performer):

    # podcast_data = {
    #     "audio":"./audio/xarmatiropunk-2021-11-16_compressed.mp3",
    #     "filename":"xarma-tiro-punk-031-asko-falta-da",
    #     "thumb":"./audio/thumb.jpeg",
    #     "caption":"Xarma tiro punk #031 Asko falta da?",
    #     "performer":"xarma tiro punk",
    # }


    bot = telegram.Bot(token=TELEGRAM_BOT_API_KEY)
    # bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    bot.send_audio(chat_id=TELEGRAM_CHAT_ID, 
        audio=open(audio, 'rb'), 
        thumb=open(thumb, 'rb'), 
        caption=caption,
        filename=filename,
        performer=performer)
    print("Telegram notification sent")
    # import pdb; pdb.set_trace()


if __name__ == '__main__':
    news_items = get_news_items()
    
    if len(news_items) > 0:
        # message = "New podcast available: " + news_items[0]["title"]
        # print(message)
        for item in news_items:
            print("Irratsaio berria: " + item["title"])
            audio_file_url = download_from_url(item['audio_url'], './audio/'+item['slug']+'.mp3')
            print("Audio irratsaioa deskargatua: " + audio_file_url)
            thumb_file_url = download_from_url(item['thumb_url'], './audio/thumb.jpeg')
            print("Irratsaioaren irudia deskargatua: " + thumb_file_url)
            if audio_file_url:
                print("Audioa konprimatzen...")
                compressed_file_url = compress_audio_url(audio_file_url, './audio/compressed/'+item['slug']+'.mp3')
                print("Audioa konprimatu da: " + compressed_file_url)
            
                notify_telegram(
                    audio=compressed_file_url,
                    filename=item['slug'],
                    thumb=thumb_file_url,
                    caption=item['title'],
                    performer=item['author'],
                )
                save_item_to_file(item)
                print("Irratsaioa gorde da")
            # import pdb; pdb.set_trace()
            # compress_audio_url("./audio/xarmatiropunk-2021-11-16.mp3", "./audio/compressed/xarmatiropunk-2021-11-16.mp3")
    # notify_telegram('Kaixo mundua')