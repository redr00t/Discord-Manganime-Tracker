from Modules.utils import get_source_url
import requests
from bs4 import BeautifulSoup

def get_last_episode_and_name_animeyt(source):
    try:
        response = requests.get(get_source_url(source, "YT"))
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        # Obtener la descripción desde "<meta property="og:description">"
        description_node = soup.find("meta", property="og:description")
        description = description_node["content"] if description_node else ""

        # Obtener la imagen desde "<meta property="og:image">"
        image_node = soup.find("meta", property="og:image")
        image_url = image_node["content"] if image_node else None

        # Obtener el número del último capítulo desde "li data-index="0""
        episode_node = soup.find("li", {"data-index": "0"})
        episode_number = episode_node.find("div", class_="epl-num").get_text() if episode_node else None

        if episode_number is not None:
            return episode_number, source['Name'], image_url, description.strip()
        else:
            print(f"Error: No se pudo encontrar el número del último capítulo en el contenido HTML.")
            return None, None, None, None
    except Exception as e:
        print(f"Error al obtener información del episodio desde AnimeYT: {str(e)}")
        return None, None, None, None
