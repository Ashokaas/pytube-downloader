"""Fichier principal de l'application pytube-downloader
"""

# Librairie(s) utilisée(s)
from flask import Flask, render_template


# Création des objets Flask et Bdd
app = Flask(__name__, template_folder="templates", static_folder="static")


# Les routes associées aux fonctions
@app.route("/")
def accueillir():
    """Gère l'accueil des utilisateurs"""

    # Rendu de la vue
    return render_template("index.html")

@app.route("/download")
def download():
    """Récupère l'URL entrée par l'utilisateur et la télécharge"""

    # Récupération de l'URL
    url = request.form["url"]

    # Rendu de la vue
    """ TODO : ajuster les noms en fonction de la template
    et traiter l'URL avec l'objet de pytube.py """
    return render_template("index.html", video="oui")

# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python

# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
