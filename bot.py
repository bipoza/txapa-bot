import telegram
from constants import TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID
from audio_compressor import compress_audio_url
from image_compressor import compress_image
from get_rss import get_news_items
from utils import create_folder, download_from_url, get_file_extension, save_item_to_file, remove_folder, create_folder





def notify_telegram(title, audio, filename, thumb, caption, performer):

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
        title=title,
        caption=caption,
        filename=filename,
        performer=performer)
    print("Telegram notification sent")
    # import pdb; pdb.set_trace()


if __name__ == '__main__':
    # RSS eta Datu basearen arteko elementu berriak ekarri
    news_items = get_news_items()
    
    if len(news_items) > 0:
        for item in news_items:
            print("Irratsaio berria: " + item["title"] +"\n")
            folder_path = "./audio/{}".format(item["id"])
            create_folder(folder_path)

            thumb_file_url = download_from_url(item['thumb_url'], '{}/{}_thumb{}'.format(folder_path, item['slug'], get_file_extension(item['thumb_url'])))
            compress_image(thumb_file_url, 30)
            
            print("Irudia deskargatua: " + thumb_file_url+"\n")

            audio_file_url = download_from_url(item['audio_url'], '{}/{}{}'.format(folder_path, item['slug'], get_file_extension(item['audio_url'])))
            print("Audio deskargatuta: " + audio_file_url +"\n")

            if audio_file_url:
                print("Audioa konprimatzen...")
                compressed_file_url = compress_audio_url(audio_file_url, '{}/{}_compressed{}'.format(folder_path, item['slug'], get_file_extension(item['audio_url'])))
                print("Audioa konprimatu da: " + compressed_file_url)
            
                notify_telegram(
                    audio=compressed_file_url,
                    filename=item['slug'],
                    thumb=thumb_file_url,
                    caption=item['caption'],
                    title=item['title'],
                    performer=item['author'],
                )
                # import pdb; pdb.set_trace()
                save_item_to_file(item)
                remove_folder(folder_path)
    else:
        print("Ez dago irratsaio berririk")
            # compress_audio_url("./audio/xarmatiropunk-2021-11-16.mp3", "./audio/compressed/xarmatiropunk-2021-11-16.mp3")
    # notify_telegram('Kaixo mundua')