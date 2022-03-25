# Imports pytube and gets link and resolution.
from pytube import YouTube
URL = input("Enter video link: ")
res = input("Enter resolution: ")
video = YouTube(URL)
# Downloads the video.
video_streams = video.streams.get_by_resolution(res)
print(video_streams.title)
video_streams.download()