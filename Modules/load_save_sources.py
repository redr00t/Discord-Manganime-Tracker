from Modules.utils import get_source_url
import json

def load_sources(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            sources = json.load(file)
            return sources if sources else []
    except FileNotFoundError:
        return []

def save_sources(file_path, sources):
    with open(file_path, 'w') as file:
        json.dump(sources, file, indent=4)