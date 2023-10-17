from Modules.utils import SourceType, get_source_url
from Modules.discord_webhook import send_discord_notification
from Modules.load_save_sources import load_sources, save_sources
import requests
from bs4 import BeautifulSoup

def check_manga_updates(sources):
    try:
        # Obtener la página web
        with requests.Session() as session:
            page_content = session.get("https://tvymanga2.com/").text

        # Analizar el contenido HTML
        soup = BeautifulSoup(page_content, 'html.parser')

        # Obtener la lista de mangas y últimos capítulos
        manga_list = soup.select("nav[aria-label='Ultimos Mangas'] ul li a")

        if manga_list:
            for manga_node in manga_list:
                manga_link = manga_node.get('href', '')
                manga_name_and_chapter = manga_node.text.strip()

                # Dividir el nombre del manga y el número del capítulo
                parts = manga_name_and_chapter.split(' ')
                if len(parts) >= 2:
                    manga_name = ' '.join(parts[:-1])
                    chapter_number_str = parts[-1]

                    # Compara con las fuentes en sources.json
                    for source in sources:
                        if source['Type'] == SourceType.Manga and source['Name'] == manga_name:
                            if chapter_number_str.isdigit():
                                chapter_number = int(chapter_number_str)
                                if source['LastEpisode'] is None or chapter_number > source['LastEpisode']:
                                    description = source.get('Description', "Descripción no disponible")
                                    image_url = source.get('ImageUrl', '')  # Obtener el URL de la imagen
                                    send_discord_notification(manga_name, chapter_number, source, image_url, description)
                                    source['LastEpisode'] = chapter_number
                            break

        save_sources("sources.json", sources)
    except Exception as e:
        print(f"Error al verificar las actualizaciones de manga: {str(e)}")