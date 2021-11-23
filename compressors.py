# Lortu beharreko tamaina maximoa: 200kb
from PIL import Image
def compress_image(image_path, quality=50):
    picture = Image.open(image_path)
    picture.save(image_path, optimize=True,quality=quality)


# Lortu beharreko tamaina maximoa: 50mb
from pydub import AudioSegment
def compress_audio_url(input_url, output_url):
    sound = AudioSegment.from_file(input_url)
    sound.export(output_url, format="mp3", parameters=["-q:a", "8"]) # 8 is the lowest quality
    return output_url