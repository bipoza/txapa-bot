from constants import BIDALITAKO_IRRATSAIOEN_DB, DEFAULT_RSS_LENGTH


# Fitxategien izenak berrizendatzeko erabiltzen da.
# Irratsaioaren izenburua pasatuta espazioak eta karaktere bereziak garbituko ditu.
def slugify(text):
    non_url_safe = ['"', '#', '$', '%', '&', '+',
                        ',', '/', ':', ';', '=', '?',
                        '@', '[', '\\', ']', '^', '`',
                        '{', '|', '}', '~', "'", "."]
    """
    Turn the text content of a header into a slug for use in an ID
    """
    non_safe = [c for c in text if c in non_url_safe]
    if non_safe:
        for c in non_safe:
            text = text.replace(c, '')
    # Strip leading, trailing and multiple whitespace, convert remaining whitespace to _
    text = u'_'.join(text.split())
    return text


def download_from_url(url, path):
    import urllib.request
    urllib.request.urlretrieve(url, path)
    return path

def get_file_extension(filename):
    import os
    return os.path.splitext(filename)[1]



# def remove_file(path):
#     import os
#     if os.path.exists(path):
#         os.remove(path)
#     else:
#         print("The file does not exist")


def create_folder(path):
    import os
    if not os.path.exists(path):
        os.makedirs(path)

def remove_folder(path):
    import os, shutil
    if os.path.exists(path):
        shutil.rmtree(path)
    else:
        print("The folder does not exist")

# JSON objektu oso bat fitxategian gordetzeko erabiltzen da. Adib: [{}, {}, {}]
def save_json_to_file(json_db, path):
    import json
    with open(path, 'w') as f:
        json.dump(json_db, f)

# JSON objektu bat fitxategitik irakurtzeko erabiltzen da.
def get_json_from_file(path):
    import json
    with open(path, 'r') as f:
        return json.load(f)


def get_mouth_number_from_string(string):
    mouth = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i, m in enumerate(mouth):
        if m in string:
            return i + 1
    return None



def add_irratsaioa_to_db(item):
    json_db = get_json_from_file(BIDALITAKO_IRRATSAIOEN_DB)
    json_db.append(item)
    # save_json_to_file(json_db, BIDALITAKO_IRRATSAIOEN_DB)

    default_rss_length = get_json_from_file(DEFAULT_RSS_LENGTH).get("length", None)

    # get recent default_rss_length items and remove oldest
    json_db = json_db[-default_rss_length:]
    save_json_to_file(json_db, BIDALITAKO_IRRATSAIOEN_DB)
