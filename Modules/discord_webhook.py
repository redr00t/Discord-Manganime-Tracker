from Modules.utils import SourceType, get_source_url
import requests

# Obtener el valor de la variable de entorno WEBHOOK_URL
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

def send_discord_notification(name, episode_number, source, image_url, description):
    try:
        # Limitar la descripción a 1024 caracteres y agregar "..." si es necesario
        if description and len(description) > 1024:
            description = description[:1021] + "..."

        if 'Source' in source and source['Source'] == 'YT':
            episode_link = f"https://animeyt.es/anime/{source['Url']}-capitulo-{episode_number}"
        else:
            episode_link = f"https://www3.animeflv.net/ver/{source['Url']}-{episode_number}" if source['Type'] == SourceType.Anime else get_source_url(source) + f"-{episode_number}"
            
        type_str = "ANIME" if source['Type'] == SourceType.Anime else "MANGA"

        # Determinar si usar "capítulo" o "episodio" basado en el tipo
        episode_type = "episodio" if source['Type'] == SourceType.Anime else "capítulo"

        # Obtener la lista de usuarios a etiquetar
        users_to_tag = source.get("UsersToTag", [])

        # Crear menciones de usuario
        user_mentions = [f"<@{user_id}>" for user_id in users_to_tag]

        # Modificar el formato del enlace para mostrarlo como texto
        link_text = f"[{name} - {episode_type.capitalize()} {episode_number}]({episode_link})"

        embed = {
            "title": f"¡Nuevo {episode_type} de {name} disponible!",
            "url": episode_link,
            "fields": [
                {"name": "Título", "value": name, "inline": True},
                {"name": "Tipo", "value": type_str, "inline": True},
                {"name": f"Número de {episode_type.capitalize()}", "value": str(episode_number), "inline": True},
                {"name": f"Ver {episode_type.capitalize()}", "value": link_text, "inline": True},
                {"name": "Descripción", "value": description or "", "inline": False}
            ],
            "thumbnail": {"url": image_url or ""}
        }

        data = {
            "content": " ".join(user_mentions),
            "embeds": [embed]
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(WEBHOOK_URL, json=data, headers=headers)

        if response.status_code != 204:
            print(f"Error al enviar la notificación a Discord: {response.text}")
    except Exception as e:
        print(f"Error al enviar la notificación a Discord: {str(e)}")