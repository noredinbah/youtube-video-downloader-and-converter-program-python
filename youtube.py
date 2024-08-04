print("Welcome to YouTube Downloader and Converter")
print("Loading...")

from pytube import YouTube
from moviepy.editor import VideoFileClip

def convert(path, pathaudio):
    video = VideoFileClip(path)
    audio = video.audio
    audio.write_audiofile(pathaudio)
    print(f"Audio was successfully extracted and saved to {pathaudio}")

def youtubevideo(link, quality):
    try:
        video = YouTube(link)
        stream = video.streams.filter(res=quality).first()
        if not stream:
            print(f"Requested quality {quality} is not available for this video.")
            return
        stream.download()
        print("Video was downloaded successfully")
    except Exception as e:
        print(f"Failed to download video: {e}")

def YoutubeAudioDownload(video_url):
    try:
        video = YouTube(video_url)
        audio = video.streams.filter(only_audio=True).first()
        if not audio:
            print("No audio streams available for this video.")
            return
        audio.download()
        print("Audio was downloaded successfully")
    except Exception as e:
        print(f"Failed to download audio: {e}")

print('''
Please choose:

(1) Download YouTube Video
(2) Download YouTube Video and Convert Into MP3
(3) Convert a local video to MP3

Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads!

Copyright (c) Noredineba 2020
''')

choice = input("Choice: ")
if choice == '1':
    link = input("Enter your link: ")
    quality = input("Choose a quality: 360p, 480p, 720p, 1080p \n")
    youtubevideo(link, quality)
elif choice == '2':
    linkaudio = input("Enter your link: ")
    YoutubeAudioDownload(linkaudio)
elif choice == '3':
    path = input("Enter the path to your video: ")
    pathaudio = input("Enter the path where you want to download the audio: ")
    convert(path, pathaudio)
else:
    print("Invalid choice")
