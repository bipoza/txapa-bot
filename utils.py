# Fitxategien izenak berrizendatzeko erabiltzen da.
# Irratsaioaren izenburua pasatuta espazioak eta karaktere bereziak garbituko ditu.
non_url_safe = ['"', '#', '$', '%', '&', '+',
                    ',', '/', ':', ';', '=', '?',
                    '@', '[', '\\', ']', '^', '`',
                    '{', '|', '}', '~', "'", "."]

def slugify(text):
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

def save_item_to_file(item):
    from get_rss import get_rss_items_in_json_from_file, save_rss_items_in_json_to_file
    json_db = get_rss_items_in_json_from_file()
    json_db.append(item)
    save_rss_items_in_json_to_file(json_db)

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
