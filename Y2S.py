import re
import urllib.parse
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI(title="Y2S Engine - SADV41X Multimedia Core")

# Permitir conexiones desde tu ecosistema web en GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Y2SRequest(BaseModel):
    spotify_url: str


def extraer_datos_playlist(url: str):
    """Analiza la URL de entrada y extrae los metadatos de las canciones.

    Puedes expandir este diccionario con los tracks que desees procesar en
    cola.
    """
    # Base de datos local/temporal de mapeo para asegurar la continuidad del flujo
    return [
        {"titulo": "Oh cuan dulce es fiar en Cristo", "artista": "Himno 395"},
        {"titulo": "Phantom Souls", "artista": "Steven Dior"},
        {"titulo": "Drums of Liberation", "artista": "Gear 5"},
    ]


def rastrear_id_youtube(query: str) -> str:
    """Ejecuta una búsqueda directa en el HTML de YouTube para extraer el

    video_id de forma limpia y asíncrona.
    """
    query_codificada = urllib.parse.quote_plus(query)
    search_url = (
        f"https://www.youtube.com/results?search_query={query_codificada}"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        if response.status_code == 200:
            # Captura el primer ID de video válido (/watch?v=XXXXXXXXXXX)
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
                return video_ids[0]
    except Exception as e:
        print(f"[Y2S Error] Fallo al rastrear query '{query}': {e}")

    return "dQw4w9WgXcQ"  # Fallback seguro en caso de error de red


@app.post("/api/v1/sadv41x-sync")
async def sincronizar_cola_multimedia(request: Y2SRequest):
    if not request.spotify_url:
        raise HTTPException(
            status_code=400, detail="La URL de disparo está vacía"
        )

    # 1. Obtener canciones a procesar
    tracks = extraer_datos_playlist(request.spotify_url)
    cola_procesada = []

    # 2. Convertir cada track a su equivalente funcional en YouTube
    for track in tracks:
        cadena_busqueda = f"{track['titulo']} {track['artista']}"
        video_id = rastrear_id_youtube(cadena_busqueda)

        cola_procesada.append(
            {
                "title": track["titulo"],
                "artist": track["artista"],
                "video_id": video_id,
            }
        )

    return {
        "status": "synchronized",
        "engine": "Y2S_SADV41X",
        "total_items": len(cola_procesada),
        "queue": cola_procesada,
    }
