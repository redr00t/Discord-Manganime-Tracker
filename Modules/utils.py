class SourceType:
    Anime = "Anime"
    Manga = "Manga"

def get_source_url(source, source_type=None):
    # AnimeYT se utiliza como fuente alternativa a AnimeFLV, hay algunos animes que debido a derechos de autor no estan presentes en esta plataforma.
    if source['Type'] == SourceType.Anime:
        if source_type == 'YT':
            return f"https://animeyt.es/tv/{source['Url']}"
        else:
            return f"https://www3.animeflv.net/anime/{source['Url']}"
    elif source['Type'] == SourceType.Manga:
        return f"https://tvymanga2.com/{source['Url']}"