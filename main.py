"""Main file of the pytube-downloader"""

# Main library that allows communication between the web site and the ytvideo downloader 
from flask import Flask, render_template, request

# Internal libraries
import video_utils
import ytvideo


# Creating Flask's object
app = Flask(__name__, template_folder="templates", static_folder="static")

# Useful features

# Associating routes to function
@app.route("/")
def welcome() -> None:
    """Welcome user"""

    # Returning web site with keywards
    return render_template("index.html", datas=None)

@app.route("/convert", methods=["POST"])
def convert() -> None:
    """Get URL from user then ask for parameters"""

    # Dictionary containing all the needed datas
    datas = {}

    # Getting URL
    link = request.form["link"]
    data = video_utils.VideoData(link=link)
    downloader = ytvideo.YTVideo(str(link))

    # Adding video's title and miniature
    datas["title"] = downloader.get_title()
    datas["miniature"] = data.get_miniature()

    # Getting audios and videos qualities
    choice = {}
    choice["audio"] = {"mp4": downloader.get_audio_qualities("mp4"),
     "webm": downloader.get_audio_qualities("webm")}
    choice["video"] = {"mp4": downloader.get_video_qualities("mp4"),
     "webm": downloader.get_video_qualities("webm")}

    # Adding video's qualities choice
    datas["choice"] = choice

    # Returning web site with keywards
    return render_template("index.html", datas=datas)

# Launching server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
