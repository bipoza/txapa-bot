def compressAudioUrl(input_url, output_url, bitrate="128k"):
    from pydub import AudioSegment
    sound = AudioSegment.from_file(input_url)
    sound.export(output_url, format="mp3", parameters=["-q:a", "8"]) # 8 is the lowest quality
    # bitrate=bitrate
    return {"status":"ok", "output_url": output_url}