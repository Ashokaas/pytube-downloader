import pytube
from video_utils import fuse_video_audio
import os


def vid_quality_string(res: str, fps: int):
    return res + str(fps)


class YTVideo:

    def __init__(self, link: str):
        self.link = link
        self.final = None
        self.video = None
        self.audio = None

        self.video_object = pytube.YouTube(link)
        self.streams = self.video_object.streams
        stream: pytube.Stream

        self.video_qualities = {"webm": {
            vid_quality_string(stream.resolution, stream.fps): stream
            for stream in self.streams.filter(adaptive=True, mime_type="video/webm")
        },
            "mp4": {
            vid_quality_string(stream.resolution, stream.fps): stream
            for stream in self.streams.filter(adaptive=True, mime_type="video/mp4")
        }}

        self.audio_qualities = {"webm": {
            stream.abr: stream
            for stream in self.streams.filter(adaptive=True, mime_type="audio/webm")
        },
            "mp4": {
            stream.abr: stream
            for stream in self.streams.filter(adaptive=True, mime_type="audio/mp4")
        }}

    def download(self, destination_folder: str, video_quality: str, audio_quality: str, file_type="mp4"):
        """
        Downloads the video

        Parameters:
            destination_folder (str): Path to the folder where the audio, video and final files will go (ex: among/us/)
            video_quality (str): the quality of the video (ex: 1080p60 / 360p)
            audio_quality (str): the quality of the audio (ex: 128kbps / 160kbps)
            file_type (str): The format of the output, either webm or mp4

        The list of the availabe qualities can be requested using the get_video/audio_qualities functions
        """
        if video_quality not in self.get_video_qualities(file_type) or audio_quality not in self.get_audio_qualities(
                file_type):
            return False
        self.video = self.video_qualities[file_type][video_quality].download(destination_folder + "video/")
        self.audio = self.audio_qualities[file_type][audio_quality].download(destination_folder + "audio/")
        self.final = fuse_video_audio(self.video, self.audio,
                                destination_folder + self.video_object.title.replace(" ", "_") + "_final." + file_type)


    def get_video_qualities(self, file_type: str):
        """
        Get available video qualities for the file_type extension (webm or mp4)
        """
        return list(self.video_qualities[file_type].keys())

    def get_audio_qualities(self, file_type: str):
        """
        Get available audio qualities for the file_type extension (webm or mp4)
        """
        return list(self.audio_qualities[file_type].keys())

    def __del__(self):
        os.remove(self.video)
        os.remove(self.audio)


if __name__ == "__main__":
    test = YTVideo("https://www.youtube.com/watch?v=szBxF-ewNfo")
    print(test.get_video_qualities("mp4"))
    print(test.get_audio_qualities("mp4"))
    print(test.download(os.path.dirname(__file__).replace('\\', '/') + "/test/", "720p50", "128kbps"))
