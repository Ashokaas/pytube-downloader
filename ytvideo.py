import pytube


def vid_quality_string(res: str, fps: int):
    if fps == 30:
        return res
    return res + str(fps)


class YTVideo:

    def __init__(self, link: str):
        self.link = link
        self.final = None
        self.video = None
        self.audio = None

        self.streams = pytube.YouTube(link).streams
        stream: pytube.Stream
        self.video_qualities = {vid_quality_string(stream.resolution, stream.fps) + stream.mime_type.removeprefix(
            "video/"): stream for stream in self.streams.filter(type="video", adaptive=True)}
        self.audio_qualities = {stream.abr + stream.mime_type.removeprefix("audio/"): stream for stream in
                                self.streams.filter(type="audio", adaptive=True)}

    def download(self, destination_folder, video_quality):
        pass

    def get_video_qualities(self):
        return list(self.video_qualities.keys())

    def get_audio_qualities(self):
        return list(self.audio_qualities.keys())


if __name__ == "__main__":
    test = YTVideo("https://www.youtube.com/watch?v=lB4z729EADM")
    print(test.get_video_qualities())
    print(test.get_audio_qualities())
