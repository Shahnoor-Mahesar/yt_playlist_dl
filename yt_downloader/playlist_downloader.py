from pytube import Playlist
import os

def download_playlist(url, directory):
    playlist = Playlist(url)
    for video in playlist.videos:
        video.register_on_progress_callback(progress_callback)
        stream = video.streams.filter(res='720p', mime_type='video/mp4').first()
        stream.download(directory)

def progress_callback(stream, chunk, bytes_remaining):
    progress = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    print("Download progress: {:.2f}%".format(progress))

if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLESMQx4LeD3NmTZ8D1qwQwwSp67kznl-K"
    directory = "E:\DBMS"
    if not os.path.exists(directory):
        os.makedirs(directory)
    download_playlist(url, directory)
