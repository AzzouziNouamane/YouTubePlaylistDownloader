from pytube import YouTube

#YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()


def downloadVideo(videoURL):
  yt = YouTube('https://www.youtube.com/watch?v=' + videoURL)
  yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

