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
    return render_template("index.html")

@app.route("/convert")
def convert() -> None:
    """Get URL from user then ask for parameters"""

    # Getting URL
    link = request.form["link"]
    data = video_utils.VideoData(link=link)
    downloader = ytvideo.YTVideo(data.get_link)

    # Getting audios and videos qualities
    choice = {"audio": downloader.get_audio_qualities,
    }
    choice["audio"] = downloader.get_audio_qualities()
    choice["video"] = downloader.get_video_qualities()

    # Returning web site with keywards
    return render_template("index.html", video=data, audio_choice=choice["audio"], video_choice=["video"])

# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python

# Launching server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
