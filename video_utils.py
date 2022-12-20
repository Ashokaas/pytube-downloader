import requests
from urllib.request import urlretrieve


class Link:
    """Gère et transforme les liens"""

    def __init__(self, link: str) -> None:
        self.link = self.reduce_link(link)

    def reduce_link(self, link: str) -> str:
        """Réduit le lien de la vidéo

        Args:
            link (str): lien de la vidéo

        Returns:
            str: version raccourcie du lien
        """
        prefixs_link_yt = ["https://youtu.be/", "https://youtube.com/watch?v=",
                           "https://www.youtu.be/", "https://www.youtube.com/watch?v=",
                           "&feature=share"]

        for prefix in prefixs_link_yt:
            link = link.replace(prefix, "")

        return link

    def get_link(self) -> str:
        """Renvoie le lien de la vidéo"""
        return self.link

    def get_likes_and_dislikes(self) -> dict:
        """Récupère les likes et dislikes de la vidéo

        Returns:
            dict: dictionnaire contenant les likes et dislikes (clefs : "likes" et "dislikes")
        """
        request_link = f"https://returnyoutubedislikeapi.com/votes?videoId={self.link}"
        response = requests.get(request_link)

        return response.json()

    def get_miniature(self) -> None:
        """Téléchargement de la miniature avec la meilleure qualité possible"""
        urlretrieve(f'http://img.youtube.com/vi/{self.link}/maxresdefault.jpg', "file")


if __name__ == "__main__":
    link = Link("https://www.youtube.com/watch?v=6ZfuNTqbHE8")
    link.get_likes_and_dislikes()
