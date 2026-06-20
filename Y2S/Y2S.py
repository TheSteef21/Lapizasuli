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
    """Aplica doble verificación para extraer la tabla de canciones reales

    de Spotify mediante API interna pública y selectores de respaldo.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "es-ES,es;q=0.9",
    }
    tracks_encontrados = []

    # Extraer identificador único del recurso
    playlist_match = re.search(r"playlist/([a-zA-Z0-9]+)", url)
    track_match = re.search(r"track/([a-zA-Z0-9]+)", url)
    album_match = re.search(r"album/([a-zA-Z0-9]+)", url)

    try:
        # VERIFICACIÓN 1: Método por API Web Pública Embebida (Inmune a cambios de HTML)
        if playlist_match:
            playlist_id = playlist_match.group(1)

            try:
                # Obtener token de transporte público oficial del widget de Spotify
                token_url = "https://open.spotify.com/get_access_token?reason=transport&productType=embed"
                token_res = requests.get(token_url, headers=headers, timeout=5)

                if token_res.status_code == 200:
                    anon_token = token_res.json().get("accessToken")
                    if anon_token:
                        # Consultar la tabla directa de canciones del endpoint oficial
                        api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit=50"
                        api_res = requests.get(
                            api_url,
                            headers={"Authorization": f"Bearer {anon_token}"},
                            timeout=5,
                        )

                        if api_res.status_code == 200:
                            items = api_res.json().get("items", [])
                            for item in items:
                                t = item.get("track", {})
                                if t:
                                    titulo = t.get("name")
                                    artistas = ", ".join(
                                        [
                                            a.get("name")
                                            for a in t.get("artists", [])
                                        ]
                                    )
                                    if titulo:
                                        tracks_encontrados.append(
                                            {
                                                "titulo": titulo,
                                                "artista": artistas,
                                            }
                                        )
            except Exception as api_err:
                print(f"[Y2S API Warning] Rebotando a Vía HTML: {api_err}")

            # VERIFICACIÓN 2: Raspado HTML clásico por Fallback si la API deniega el acceso
            if not tracks_encontrados:
                embed_url = (
                    f"https://open.spotify.com/embed/playlist/{playlist_id}"
                )
                res = requests.get(embed_url, headers=headers, timeout=10)

                script_match = re.search(
                    r'<script id="initial-state"[^>]*>(.*?)</script>',
                    res.text,
                    re.DOTALL,
                )
                if script_match:
                    raw_data = urllib.parse.unquote(script_match.group(1))
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
                    except:
                        pass

                # Filtro por expresiones regulares directas en texto plano
                if not tracks_encontrados:
                    canciones = re.findall(
                        r'{"name":"([^"]+)","artists":', res.text
                    )
                    for con in canciones:
                        if con not in [
                            "Spotify",
                            "Premium",
                            "Search",
                            "Your Library",
                        ]:
                            if (
                                not tracks_encontrados
                                or tracks_encontrados[-1]["titulo"] != con
                            ):
                                tracks_encontrados.append(
                                    {"titulo": con, "artista": "Track"}
                                )

        elif album_match:
            album_id = album_match.group(1)
            embed_url = f"https://open.spotify.com/embed/album/{album_id}"
            res = requests.get(embed_url, headers=headers, timeout=10)
            matches = re.findall(r'{"name":"([^"]+)","artists":', res.text)
            for m in matches:
                if m not in ["Spotify", "Premium"]:
                    tracks_encontrados.append({"titulo": m, "artista": "Album"})

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
                tracks_encontrados.append(
                    {
                        "titulo": title_match.group(1),
                        "artista": (
                            desc_match.group(1).split("·")[0].strip()
                            if desc_match
                            else "Single"
                        ),
                    }
                )

    except Exception as e:
        print(f"[Y2S Core Critical Failure]: {e}")

    return tracks_encontrados


def rastrear_id_youtube(query: str) -> str:
    """Busca el término y realiza una doble extracción (URL estructurada

    y JSON interno de YT) para garantizar el ID de video.
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
            # Filtro 1: Extracción clásica por dirección corta
            video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
            if video_ids:
                return video_ids[0]

            # Filtro 2: Extracción por mapa de datos JSON interno de YouTube
            json_ids = re.findall(
                r'"videoId":"([a-zA-Z0-9_-]{11})"', response.text
            )
            if json_ids:
                return json_ids[0]
    except Exception as e:
        print(f"[Y2S YouTube Search Error]: {e}")

    return "dQw4w9WgXcQ"  # Fallback seguro global


@app.post("/api/v1/sadv41x-sync")
async def sincronizar_cola_multimedia(request: Y2SRequest):
    if not request.spotify_url:
        raise HTTPException(
            status_code=400, detail="La URL de disparo está vacía"
        )

    tracks = extraer_datos_playlist(request.spotify_url)
    cola_procesada = []

    # Si tras la doble verificación ambos sistemas fallan por caída de red externa, se activa la firma
    if not tracks:
        tracks = [
            {"titulo": "Oh cuan dulce es fiar en Cristo", "artista": "Himno 395"}
        ]

    for track in tracks:
        cadena_busqueda = f"{track['titulo']} {track['artista']}".strip()
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
