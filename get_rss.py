import feedparser
from bs4 import BeautifulSoup
from constants import TXAPA_IRRATIA_RSS_URL
from utils import slugify
import json

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

def get_rss_items_in_json():
    feed = feedparser.parse(TXAPA_IRRATIA_RSS_URL)
    rss_items = feed.entries

    json_items = []
    for item in rss_items:
        podcast_data = {
            "id": item.get("id", None),
            "title": item.get("title", None),
            "audio_url": get_mp3_url(item),
            "thumb_url":get_thumb_url(item),
            "author": item.tags[0]['term'],
            "slug":slugify(item.title),
            "date": item.get("published", None),
            "duration": item.get("itunes_duration", None),
        }
        json_items.append(podcast_data)

    return json_items



def save_rss_items_in_json_to_file(rss_items):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(rss_items, f, ensure_ascii=False, indent=4)


def get_rss_items_in_json_from_file():
    with open("data.json", "r") as f:
        rss_items = json.load(f)
    return rss_items


def get_news_items():
    server_rss_items = get_rss_items_in_json()
    local_rss_items = get_rss_items_in_json_from_file()
    # Bi zerrendak konparatzen ditugu, bakarrik berriak direnak hatuko ditugu
    compared_new_items = [item for item in server_rss_items if item not in local_rss_items]

    print(compared_new_items)
    return compared_new_items
    # save_rss_items_in_json_to_file(rss_items)

if __name__ == "__main__":
    get_news_items()