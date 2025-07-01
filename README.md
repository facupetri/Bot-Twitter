
# Twitter Posting Bot

## English Version

### Description

This project is a simple Twitter bot that automatically posts tweets with text and optional images at regular intervals (e.g. every 3 hours).

### Requirements

- Python 3.x
- Tweepy library (`pip install tweepy`)
- Twitter Developer Account with API keys and tokens
- Folder named `media` with images to post (optional)
- A JSON or Python list file with posts (text and optional image filename)

### Setup

1. Create a Twitter Developer account and set up an app to get API Key, API Secret, Access Token, and Access Token Secret.
2. Store those credentials securely in your script or environment variables.
3. Prepare a list of posts in JSON or Python format, for example:

```json
[
  {
    "text": "Hello world! #firsttweet",
    "image": "image1.jpg"
  },
  {
    "text": "Just text, no image here."
  }
]
```

4. Place images inside the `media` folder. The `"image"` field should contain only the filename, e.g. `"image1.jpg"`.

### How to run

1. First, run `bot.py` to authenticate with your Twitter account:

```bash
python bot.py
```

You should see a message confirming the connection.

2. Then, run `scheduler.py` to start the posting loop:

```bash
python scheduler.py
```

The bot will post one tweet every 3 hours automatically.

### Troubleshooting

- If images do not post, check that the filenames in your post list match exactly the files in the `media` folder (case sensitive).
- Make sure your Twitter API keys have the right permissions (write access).
- If you get errors about missing files, check the path and clean extra quotes in your image fields.
- Logs will show what the bot is doing; review warnings and errors there.

### License

MIT License (or your preferred license)


---


# Bot para publicar en Twitter

## Versión en Español

### Descripción

Este proyecto es un bot sencillo para Twitter que publica automáticamente tweets con texto y, opcionalmente, imágenes a intervalos regulares (ej: cada 3 horas).

### Requisitos

- Python 3.x
- Biblioteca Tweepy (`pip install tweepy`)
- Cuenta de desarrollador de Twitter con claves y tokens de API
- Carpeta llamada `media` con imágenes para publicar (opcional)
- Archivo JSON o lista en Python con posts (texto y nombre opcional de imagen)

### Configuración

1. Crea una cuenta de desarrollador en Twitter y configura una app para obtener API Key, API Secret, Access Token y Access Token Secret.
2. Guarda esas credenciales de forma segura en tu script o variables de entorno.
3. Prepara una lista de posts en formato JSON o Python, por ejemplo:

```json
[
  {
    "text": "¡Hola mundo! #primerTweet",
    "image": "imagen1.jpg"
  },
  {
    "text": "Solo texto, sin imagen."
  }
]
```

4. Coloca las imágenes dentro de la carpeta `media`. El campo `"image"` debe contener sólo el nombre del archivo, por ejemplo `"imagen1.jpg"`.

### Cómo ejecutar

1. Primero, ejecutá `bot.py` para autenticarte con tu cuenta de Twitter:

```bash
python bot.py
```

Deberías ver un mensaje confirmando la conexión.

2. Luego, ejecutá `scheduler.py` para iniciar el ciclo de publicaciones:

```bash
python scheduler.py
```

El bot publicará un tweet cada 3 horas automáticamente.

### Solución de problemas

- Si las imágenes no se publican, chequeá que los nombres en tu lista coincidan exactamente con los archivos en la carpeta `media` (sensible a mayúsculas/minúsculas).
- Asegurate que las claves API de Twitter tengan permisos de escritura.
- Si hay errores por archivos faltantes, revisá la ruta y limpiá comillas extras en el campo de imagen.
- Los logs muestran lo que el bot hace; revisá advertencias y errores ahí.

### Licencia

Licencia MIT (o la que prefieras)
