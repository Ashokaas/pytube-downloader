"""Fichier principal de l'application pytube-downloader
"""

# Module principale permettant la communication entre le site web et le downloader
from flask import Flask, render_template, request

# Modules internes
import video_utils
import ytvideo


# Création des objets Flask et Bdd
app = Flask(__name__, template_folder="templates", static_folder="static")


# Les routes associées aux fonctions
@app.route("/")
def accueillir() -> None:
    """Gère l'accueil des utilisateurs"""

    # Rendu de la vue
    return render_template("index.html")

@app.route("/convert")
def convert() -> None:
    """Récupère l'URL entrée par l'utilisateur et la télécharge"""

    # Récupération de l'URL
    link = request.form["link"]
    data = video_utils.VideoData(link=link)
    choice = {}

    # Rendu de la vue
    return render_template("index.html", video=data)

# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
