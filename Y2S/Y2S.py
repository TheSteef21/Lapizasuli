import json
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
    """Escanea la URL pública de Spotify y extrae los metadatos reales de las

    canciones usando el widget de incrustación oficial.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "es-ES,es;q=0.9",
    }
    tracks_encontrados = []

    # Detectar IDs de Spotify
    playlist_match = re.search(r"playlist/([a-zA-Z0-9]+)", url)
    track_match = re.search(r"track/([a-zA-Z0-9]+)", url)

    try:
        if playlist_match:
            playlist_id = playlist_match.group(1)
            # URL de Embed oficial de Spotify
            embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
            res = requests.get(embed_url, headers=headers, timeout=10)

            # Intentar capturar los datos estructurados en el script initial-state
            script_match = re.search(
                r'<script id="initial-state"[^>]*>(.*?)</script>',
                res.text,
                re.DOTALL,
            )
            if script_match:
                raw_data = script_match.group(1)
                if "%" in raw_data:
                    raw_data = urllib.parse.unquote(raw_data)

                data = json.loads(raw_data)
                try:
                    items = data["resource"]["playlist"]["tracks"]["items"]
                    for item in items:
                        t = item.get("track", {})
                        titulo = t.get("name")
                        artistas = ", ".join(
                            [a.get("name") for a in t.get("artists", [])]
                        )
                        if titulo:
                            tracks_encontrados.append(
                                {"titulo": titulo, "artista": artistas}
                            )
                except KeyError:
                    pass

            # Salvavidas por Regex si el JSON cambia de estructura
            if not tracks_encontrados:
                matches = re.findall(
                    r'{"track":{"name":"([^"]+)","artists":\[([^\]]+)\]',
                    res.text,
                )
                for track_name, artists_raw in matches:
                    artist_names = re.findall(r'"name":"([^"]+)"', artists_raw)
                    artistas = ", ".join(artist_names)
                    tracks_encontrados.append(
                        {"titulo": track_name, "artista": artistas}
                    )

        elif track_match:
            track_id = track_match.group(1)
            embed_url = f"https://open.spotify.com/embed/track/{track_id}"
            res = requests.get(embed_url, headers=headers, timeout=10)
            title_match = re.search(
                r'<meta property="og:title" content="(.*?)"', res.text
            )
            desc_match = re.search(
                r'<meta property="og:description" content="(.*?)"', res.text
            )
            if title_match:
                titulo = title_match.group(1)
                artista = (
                    desc_match.group(1).split("·")[0].strip()
                    if desc_match
                    else ""
                )
                tracks_encontrados.append(
                    {"titulo": titulo, "artista": artista}
                )

    except Exception as e:
        print(f"[Y2S Engine Error] Fallo al parsear HTML de Spotify: {e}")

    # Fallback definitivo y controlado (Tu himno insignia de respaldo si falla la red)
    if not tracks_encontrados:
        tracks_encontrados.append(
            {"titulo": "Oh cuan dulce es fiar en Cristo", "artista": "Himno 395"}
        )

    return tracks_encontrados


def rastrear_id_youtube(query: str) -> str:
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
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
                return video_ids[0]
    except Exception as e:
        print(f"[Y2S Error] Fallo al rastrear query '{query}': {e}")

    return "dQw4w9WgXcQ"


@app.post("/api/v1/sadv41x-sync")
async def sincronizar_cola_multimedia(request: Y2SRequest):
    if not request.spotify_url:
        raise HTTPException(
            status_code=400, detail="La URL de disparo está vacía"
        )

    tracks = extraer_datos_playlist(request.spotify_url)
    cola_procesada = []

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
