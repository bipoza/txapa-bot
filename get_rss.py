import feedparser
from constants import TXAPA_IRRATIA_RSS_URL
from utils import slugify

def getMP3FromItem(self):
    for link in self.links:
        if link.rel == "enclosure":
            return link.href    
    return None

def getRSSItems():
    feed = feedparser.parse(TXAPA_IRRATIA_RSS_URL)
    itemf = feed.entries #[1]

    for item in itemf:
        podcast_data = {
            "title": item.title,
            "audio_url": getMP3FromItem(item),
            "author": item.tags[0]['term'],
            "thumb":"",
            "slug":slugify(item.title)

        }
        # print(slugify(item.title))
        import pdb; pdb.set_trace()


getRSSItems()