from pytube import YouTube
import os

def download_video(url, directory):
    video = YouTube(url)
    video.register_on_progress_callback(progress_callback)
    stream = video.streams.filter(res='720p', mime_type='video/mp4').first()
    stream.download(directory)

def progress_callback(stream, chunk, bytes_remaining):
    progress = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    print("Download progress: {:.2f}%".format(progress))

if __name__ == "__main__":
    url = "https://youtu.be/aRwrdbcAh2s"
    directory = "D:\youtube VIDS"
    if not os.path.exists(directory):
        os.makedirs(directory)
    download_video(url, directory)
