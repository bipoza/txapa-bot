from compressors import compress_audio_url, compress_image
from get_rss import get_news_items
from utils import create_folder, download_from_url, get_file_extension, add_irratsaioa_to_db, remove_folder
from telegram_sender import send_audio_to_chat


def new_podcast_checker_task():
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
            
                send_audio_to_chat(
                    audio=compressed_file_url,
                    filename=item['slug'],
                    thumb=thumb_file_url,
                    caption=item['caption'],
                    title=item['title'],
                    performer=item['author'],
                    duration=item['duration']
                )
                
                add_irratsaioa_to_db(item)
                remove_folder(folder_path)
    else:
        print("Ez dago irratsaio berririk")