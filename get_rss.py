import feedparser
from bs4 import BeautifulSoup
from constants import DEFAULT_RSS_LENGTH, TXAPA_IRRATIA_RSS_URL, BIDALITAKO_IRRATSAIOEN_DB
from utils import save_json_to_file, slugify, get_json_from_file, get_mouth_number_from_string

def get_id(item):
    id= item.get("id", None)
    if id:
        return id.split("?p=",1)[1] 
    return None

def get_mp3_url(item):
    for link in item.links:
        if link.rel == "enclosure":
            return link.href    
    return None


def get_thumb_url(item):
    soup = BeautifulSoup(item.summary, features="html.parser")
    img = soup.find('img')
    if img:
        return img['src']
    return None

def get_duration_in_seconds(item):
    duration = item.get("itunes_duration", None)
    if duration:
        duration_parts = duration.split(":")
        if len(duration_parts) == 3:
            return int(duration_parts[0]) * 3600 + int(duration_parts[1]) * 60 + int(duration_parts[2])
        elif len(duration_parts) == 2:
            return int(duration_parts[0]) * 60 + int(duration_parts[1])
        else:
            return int(duration_parts[0])
    return None

def get_caption(item):
    soup = BeautifulSoup(item.summary, features="html.parser")
    caption = soup.find('p')
    if caption:
        return caption.text
    return None

def get_date_in_format(item):
    date = item.get("published", None)
    if date:
        # parse Tue, 09 Nov 2021 22:24:02 +0000 date format to yyyy-mm-dd hh:mm:ss
        date_parts = date.split(" ")
        return date_parts[3] + "-" + str(get_mouth_number_from_string(date_parts[2])) + "-" + date_parts[1] + " " + date_parts[4]
    return None

def get_rss_items_in_json():
    feed = feedparser.parse(TXAPA_IRRATIA_RSS_URL)
    rss_items = feed.entries 
    # [: : -1] funtzioak zerrendaren ordena aldatzen du. Zaharrak lehenengo eta ondoren berriak. .reverse() modukoa da.
    rss_items = rss_items[: : -1]
    json_items = []
    for item in rss_items:
        podcast_data = {
            "id": get_id(item),
            "title": item.get("title", None),
            "audio_url": get_mp3_url(item),
            "thumb_url":get_thumb_url(item),
            "author": item.tags[0]['term'],
            "slug":slugify(item.title),
            "date": get_date_in_format(item),
            "duration": get_duration_in_seconds(item),
            "caption": get_caption(item),
        }

        json_items.append(podcast_data)
    save_json_to_file({"length": len(json_items)}, DEFAULT_RSS_LENGTH)
    return json_items

def get_news_items():
    server_rss_items = get_rss_items_in_json()
    local_rss_items = get_json_from_file(BIDALITAKO_IRRATSAIOEN_DB)
    # Bi zerrendak konparatzen ditugu, bakarrik berriak direnak hatuko ditugu
    compared_new_items = [item for item in server_rss_items if item not in local_rss_items]
    return compared_new_items

if __name__ == "__main__":
    get_news_items()
    # json = get_rss_items_in_json()
    # import pdb; pdb.set_trace()