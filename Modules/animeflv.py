from Modules.utils import SourceType, get_source_url
import requests
from bs4 import BeautifulSoup
import re

def get_last_episode_and_name_animeflv(source):
    try:
        response = requests.get(get_source_url(source))
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        image_node = soup.find("meta", {"property": "og:image"})
        image_url = image_node["content"] if image_node else None

        # Obtener la descripción de la sección <div class="Description">
        description_node = soup.find("div", class_="Description")
        description = description_node.get_text(strip=True) if description_node else ""

        episode_match = re.search(r'var episodes = \[\[([0-9]+)', content)

        if episode_match:
            episode_number = int(episode_match.group(1))
            return episode_number, source['Name'], image_url, description
        else:
            return None, None, None, None
    except Exception as e:
        print(f"Error al obtener información del episodio: {str(e)}")
        return None, None, None, None