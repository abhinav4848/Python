import sys
import youtube_dl
import os

os.chdir("D:/downloads")

options = {
    'format': 'bestaudio/best',
    'extractaudio': True,  # only keep the audio
    'audioformat': "mp3",  # convert to mp3
    # name the file, the ID of the video, then ext
    'outtmpl': '%(title)s_%(id)s.%(ext)s',
    'noplaylist': True,    # only download single song, not playlist
}

while True:
    try:
        youtube_url = sys.argv[1]
    except:
        print('Sorry, not valid input. Try again')
        break
    else:
        if youtube_url == '':
            continue
        else:
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([youtube_url])
            break
    finally:
        print('Created by Abhinav, 2019')
        print("Downloaded to "+os.getcwd())
