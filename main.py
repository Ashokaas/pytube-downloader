"""Fichier principal de l'application pytube-downloader
"""

# Librairie(s) utilisée(s)
from flask import *


# Création des objets Flask et Bdd
app = Flask(__name__, template_folder="templates", static_folder="static")


# Les routes associées aux fonctions
@app.route("/")
def accueillir():
    """Gère l'accueil des utilisateurs"""
    
    # Rendu de la vue
    return render_template("accueil.html")

# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)