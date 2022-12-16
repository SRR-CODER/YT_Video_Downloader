import os

from moviepy.editor import VideoFileClip, AudioFileClip
from pytube import YouTube


def download(url):
    yt_object = YouTube(url)
    video_title = yt_object.title

    video = yt_object.streams.filter(mime_type="video/mp4").order_by('resolution').desc().first().download()
    audio = yt_object.streams.filter(mime_type="audio/webm").order_by('itag').desc().first().download()

    vid_clip = VideoFileClip(video)
    aud_clip = AudioFileClip(audio)

    merged_clip = vid_clip.set_audio(aud_clip)

    merged_clip.write_videofile(f'{video_title} (downloaded).mp4')
    os.remove(video)
    os.remove(audio)


link = input("Please enter the YouTube video link here: ")
download(link)
