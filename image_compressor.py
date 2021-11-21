def compress_image(image_path, quality=50):
    import io
    from PIL import Image
    picture = Image.open(image_path)
    picture.save(image_path, optimize=True,quality=quality) 


# compress_image('./audio/27665/HAUS_OF_BEATS_279_thumb.jpg', quality=50)
# 247,2 kB (247.159 byte)