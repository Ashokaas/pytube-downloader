"""File managing links"""
import requests
from urllib.request import urlretrieve
import subprocess
from moviepy.config import get_setting


class VideoData:
    """Getting and transforming link"""

    def __init__(self, link: str) -> None:
        self.link = self.reduce_link(link)

    def reduce_link(self, link: str) -> str:
        """Reducing video's link

        Args:
            link (str): video's link

        Return:
            str: short link's version
        """
        prefixs_link_yt = ["https://youtu.be/", "https://youtube.com/watch?v=",
                           "https://www.youtu.be/", "https://www.youtube.com/watch?v=",
                           "&feature=share"]

        for prefix in prefixs_link_yt:
            link = link.replace(prefix, "")

        return link

    def get_link(self) -> str:
        """Return video's link"""
        return self.link

    def get_likes_and_dislikes(self) -> dict:
        """Getting video's likes and dislikes

        Returns:
            dict: dictionary containing likes and dislikes (keys : "likes", "dislikes")
        """
        request_link = f"https://returnyoutubedislikeapi.com/votes?videoId={self.link}"
        response = requests.get(url=request_link, timeout=30)
        
        return response.json()

    def get_miniature(self) -> None:
        """Miniature's download with maximum available resolution"""
        return f'http://img.youtube.com/vi/{self.link}/maxresdefault.jpg'


def fuse_video_audio(video, audio, output, vcodec='copy', acodec='copy'):
    """
    Fuses a video and audio file into one video file.

    Parameters:
        video (str): Path to the video file
        audio (str): Path to the audio file
        output (str): Path to the output file
        vcodec (str): ignore that
        acodec (str): unless you know what you are doing
    """
    cmd = [get_setting("FFMPEG_BINARY"), "-y", "-i", audio, "-i", video, "-vcodec", vcodec, "-acodec", acodec, output]
    subprocess.call(cmd)
    return output


if __name__ == "__main__":
    data = VideoData("https://www.youtube.com/watch?v=6ZfuNTqbHE8")
    data.get_likes_and_dislikes()