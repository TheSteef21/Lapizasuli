from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import re

app = FastAPI(title="SADV41X Core Web Service")

# Permitir que tu frontend en GitHub Pages acceda al servicio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlaylistRequest(BaseModel):
    spotify_url: str

def obtener_tracks_spotify(url: str):
    """
    Simulación/Extracción de metadatos de la playlist de Spotify.
    En producción, puedes usar la API oficial de Spotify (spotipy) 
    o un parser de respaldo si es un entorno cerrado.
    """
    # Ejemplo de estructura de retorno simulada basada en el procesamiento de la URL
    # Aquí puedes integrar 'spotipy' con Client ID/Secret de ser necesario.
    return [
        {"titulo": "Oh cuan dulce es fiar en Cristo", "artista": "Himno"},
        {"titulo": "Phantom Souls", "artista": "Steven Dior"},
        {"titulo": "Drums of Liberation", "artista": "Gear 5"}
    ]

def buscar_en_youtube(query: str):
    """
    Busca en YouTube el equivalente de la canción y extrae el ID del video.
    """
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        # Extraer el primer video_id usando expresiones regulares en el HTML de respuesta
        video_ids = re.findall(r"watch\?v=(\S{11})", response.text)
        if video_ids:
            return f"https://www.youtube.com/watch?v={video_ids[0]}"
    except Exception as e:
        print(f"Error buscando en YT: {e}")
    return None

@app.post("/api/v1/process-playlist")
async def process_playlist(request: PlaylistRequest):
    if not request.spotify_url:
        raise HTTPException(status_code=400, detail="URL de Spotify inválida")
    
    # 1. Obtener canciones de Spotify
    tracks = obtener_tracks_spotify(request.spotify_url)
    playlist_procesada = []
    
    # 2. Mapear cada canción a su enlace de YouTube
    for track in tracks:
        query_busqueda = f"{track['titulo']} {track['artista']}"
        yt_url = buscar_en_youtube(query_busqueda)
        
        if yt_url:
            # Extraer ID para el reproductor de fondo
            video_id = yt_url.split("v=")[-1]
            playlist_procesada.append({
                "title": track["titulo"],
                "artist": track["artista"],
                "yt_url": yt_url,
                "video_id": video_id
            })
            
    return {
        "status": "success",
        "total_tracks": len(playlist_procesada),
        "queue": playlist_procesada
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
