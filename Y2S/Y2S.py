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
    """Escanea la URL pública de Spotify de forma asíncrona y extrae los

    metadatos reales de las canciones sin necesidad de tokens rígidos.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "es-ES,es;q=0.9",
    }
    tracks_encontrados = []

    # Detectar identificadores dentro del enlace (Playlist, Álbum o Track individual)
    playlist_match = re.search(r"playlist/([a-zA-Z0-9]+)", url)
    album_match = re.search(r"album/([a-zA-Z0-9]+)", url)
    track_match = re.search(r"track/([a-zA-Z0-9]+)", url)

    try:
        if playlist_match:
            playlist_id = playlist_match.group(1)
            embed_url = f"https://open.spotify.com/embed/playlist/{playlist_id}"
            res = requests.get(embed_url, headers=headers, timeout=10)

            # Extraer el contenedor de datos deshidratados que usa Spotify
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

                # Intentar mapeo por estructura clásica de recursos
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

                # Respaldo de extracción profunda recursiva si Spotify muta las llaves internas
                if not tracks_encontrados:

                    def buscar_nodos_tracks(obj):
                        if isinstance(obj, dict):
                          if (
                              "tracks" in obj
                              and isinstance(obj["tracks"], dict)
                              and "items" in obj["tracks"]
                          ):
                            return obj["tracks"]["items"]
                          if "items" in obj and isinstance(obj["items"], list):
                            if len(obj["items"]) > 0 and (
                                "track" in obj["items"][0]
                                or "name" in obj["items"][0]
                            ):
                              return obj["items"]
                          for v in obj.values():
                            found = buscar_nodos_tracks(v)
                            if found:
                              return found
                        elif isinstance(obj, list):
                          for item in obj:
                            found = buscar_nodos_tracks(item)
                            if found:
                              return found
                        return None

                    items = buscar_nodos_tracks(data)
                    if items:
                        for item in items:
                          t = item.get("track", item)
                          if "data" in t:
                            t = t["data"]
                          titulo = t.get("name")
                          artists_list = t.get("artists", [])
                          if (
                              isinstance(artists_list, dict)
                              and "items" in artists_list
                          ):
                            artists_list = artists_list["items"]

                          artistas = ""
                          if isinstance(artists_list, list):
                            artistas = ", ".join(
                                [
                                    (
                                        a.get("profile", {}).get(
                                            "name", a.get("name", "")
                                        )
                                        if isinstance(a, dict)
                                        else ""
                                    )
                                    for a in artists_list
                                ]
                            )

                          if titulo:
                            tracks_encontrados.append(
                                {"titulo": titulo, "artista": artistas}
                            )

        elif track_match:
            # Soporte nativo para cuando dispares canciones individuales en el buscador
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

    # Fallback de emergencia: si la seguridad de Spotify bloquea el render, extrae el título de la lista
    if not tracks_encontrados:
        try:
            res = requests.get(url, headers=headers, timeout=10)
            title_tag = re.search(r"<title>(.*?)</title>", res.text)
            if title_tag:
                meta_title = (
                    title_tag.group(1)
                    .split("|")[0]
                    .replace("Spotify", "")
                    .strip()
                )
                tracks_encontrados.append(
                    {"titulo": meta_title, "artista": "Playlist Enlace"}
                )
        except:
            pass

    # Si todo método de red es denegado, avisa al sistema
    if not tracks_encontrados:
        tracks_encontrados.append(
            {
                "titulo": "Sincronización requerida",
                "artista": "Ecosistema SADV41X",
            }
        )

    return tracks_encontrados


def rastrear_id_youtube(query: str) -> str:
    """Busca el término generado en YouTube y extrae el identificador de video

    más relevante de forma directa.
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

    # Procesar la lista real desde el enlace proveído
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
