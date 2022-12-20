import requests


class Link:
    def __init__(self, link) -> None:
        self.link = self.reduce_link(link)


    def reduce_link(self, link:str) -> str:
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
    
    
    def get_link(self):
        """Renvoie le lien de la vidéo"""
        return self.link
    
    
    def get_likes_and_dislikes(self):
        """Récupère les likes et dislikes de la vidéo

        Returns:
            dict: dictionnaire contenant les likes et dislikes (clefs : "likes" et "dislikes")
        """
        request_link = f"https://returnyoutubedislikeapi.com/votes?videoId={self.link}"
        response = requests.get(request_link)
        
        return response.json()
        
        

if __name__ == "__main__":
    link = Link("https://www.youtube.com/watch?v=6ZfuNTqbHE8")
    link.get_likes_and_dislikes()