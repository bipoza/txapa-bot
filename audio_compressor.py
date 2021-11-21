def compress_audio_url(input_url, output_url):
    from pydub import AudioSegment
    sound = AudioSegment.from_file(input_url)
    sound.export(output_url, format="mp3", parameters=["-q:a", "8"]) # 8 is the lowest quality
    return output_url