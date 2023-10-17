# Rastreador de Actualizaciones de Anime y Manga

Este proyecto es una aplicación de Python que rastrea la disponibilidad de nuevos episodios de anime y capítulos de manga en fuentes en línea específicas y notifica a través de Discord cuando se encuentran nuevas actualizaciones. También se proporciona soporte para Docker, lo que facilita su implementación y configuración.

## Funcionamiento

La aplicación consta de varios componentes:

- `main.py`: El punto de entrada de la aplicación. Carga las fuentes desde un archivo JSON, verifica periódicamente si hay nuevas actualizaciones y envía notificaciones a Discord.

- `animeflv.py` y `animeyt.py`: Contienen funciones para obtener información sobre los episodios de anime de las fuentes "AnimeFLV" y "AnimeYT".

- `discord_webhook.py`: Envía notificaciones a través de Discord utilizando webhooks. Formatea los mensajes y crea menciones de usuario si es necesario.

- `load_save_sources.py`: Contiene funciones para cargar y guardar fuentes desde y hacia un archivo JSON llamado "sources.json".

- `mangas.py`: Verifica si hay nuevas actualizaciones de manga en la fuente "tvymanga2.com".

- `utils.py`: Define una clase `SourceType` que enumera los tipos de fuentes (Anime y Manga) y una función `get_source_url` para construir la URL de las fuentes basada en el tipo y la fuente específica.

## Configuración

### Variables de Entorno

La aplicación admite la configuración a través de variables de entorno. Puedes configurar las siguientes variables de entorno en el archivo `docker-compose.yml`:

- `WEBHOOK_URL`: La URL del webhook de Discord donde se enviarán las notificaciones.

- `WAIT_TIME_SECONDS`: El intervalo de tiempo, en segundos, entre las comprobaciones de actualizaciones. El valor predeterminado es 600 segundos (10 minutos).

### Docker

Si deseas ejecutar la aplicación en un contenedor Docker, puedes utilizar el Dockerfile y el archivo `docker-compose.yml` proporcionados.

1. Asegúrate de tener Docker instalado en tu sistema.

2. Modifica el archivo `docker-compose.yml` y define las variables de entorno necesarias (WEBHOOK_URL y WAIT_TIME_SECONDS).

3. Ejecuta la aplicación utilizando Docker Compose con el siguiente comando:

   ```bash
   docker-compose up -d
   ```

La aplicación se ejecutará en un contenedor Docker y realizará comprobaciones periódicas de actualizaciones.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de abrir problemas o enviar solicitudes de extracción. Estamos abiertos a mejoras y nuevas características.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.