import json
import time
import os
from Modules.load_save_sources import load_sources, save_sources
from Modules.animeyt import get_last_episode_and_name_animeyt
from Modules.animeflv import get_last_episode_and_name_animeflv
from Modules.mangas import check_manga_updates, SourceType
from Modules.discord_webhook import send_discord_notification
from Modules.utils import SourceType

# Intervalo de comprobación de episodios y capítulos
WAIT_TIME_SECONDS = int(os.environ.get("WAIT_TIME_SECONDS", 600))

def main():
    sources = load_sources("sources.json")

    while True:
        for source in sources:
            if source['Type'] == SourceType.Anime:
                if 'Source' in source and source['Source'] == 'YT':
                    episode_number, anime_name, image_url, description = get_last_episode_and_name_animeyt(source)
                else:
                    episode_number, anime_name, image_url, description = get_last_episode_and_name_animeflv(source)

                if episode_number is None or anime_name is None or image_url is None or description is None:
                    print(f"Error al obtener el episodio para {anime_name} ({source['Url']}). Revisa la fuente.")
                    continue

                # Convierte episode_number a un número entero solo para comparar
                episode_number = int(episode_number)

                if source['LastEpisode'] is None or episode_number > int(source['LastEpisode']):
                    send_discord_notification(anime_name, episode_number, source, image_url, description)
                    source['LastEpisode'] = episode_number  # Almacenar como un número entero, no como cadena
                    print(f"Comprobado: {anime_name} ({source['Url']}) - Episodio {episode_number}")

            elif source['Type'] == SourceType.Manga:
                check_manga_updates(sources)
                print(f"Comprobado: {source['Name']} (Manga)")

        save_sources("sources.json", sources)
        time.sleep(WAIT_TIME_SECONDS)

if __name__ == "__main__":
    main()
