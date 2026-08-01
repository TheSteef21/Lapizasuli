from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import xml.etree.ElementTree as ET

app = FastAPI()

# Configuración de CORS para permitir solicitudes desde GitHub Pages y cualquier nodo externo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/sismos-panama")
async def obtener_sismos_panama():
    # URL del feed oficial RSS de la EMSC
    url = "https://www.emsc-csem.org/service/rss/rss.php?min_mag=2.0"
    
    eventos = []
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 200:
                root = ET.fromstring(response.text)
                channel = root.find("channel")
                if channel is not None:
                    for item in channel.findall("item"):
                        title = item.find("title")
                        pub_date = item.find("pubDate")
                        
                        titulo_texto = title.text if title is not None else "Sismo sin título"
                        
                        eventos.append({
                            "titulo": titulo_texto,
                            "coordenadas": [8.98, -79.52], 
                            "magnitud": "N/A",
                            "fecha": pub_date.text if pub_date is not None else str(datetime.now())
                        })
                        
        return {
            "status": "OK",
            "total": len(eventos),
            "eventos": eventos[:15]
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "total": 0,
            "eventos": [],
            "detalles": str(e)
        }
