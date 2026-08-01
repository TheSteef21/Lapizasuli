from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/sismos-panama")
async def obtener_sismos_panama():
    # API pública de la EMSC en formato JSON (últimos sismos globales con magnitud >= 2.0)
    url = "https://www.emsc-csem.org/service/rest/earthquake/search.php?min_mag=2.0&limit=20"
    
    eventos = []
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=10.0)
            if response.status_code == 200:
                data = response.json()
                features = data.get("features", [])
                
                for feature in features:
                    props = feature.get("properties", {})
                    geom = feature.get("geometry", {})
                    coords = geom.get("coordinates", [0, 0]) # [longitud, latitud, profundidad]
                    
                    eventos.append({
                        "titulo": props.get("flynn_region", "Sismo en la región"),
                        "coordenadas": [coords[1], coords[0]], # [latitud, longitud]
                        "magnitud": props.get("mag", "N/A"),
                        "fecha": props.get("time", str(datetime.now()))
                    })
                        
        return {
            "status": "OK",
            "total": len(eventos),
            "eventos": eventos
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "total": 0,
            "eventos": [],
            "detalles": str(e)
        }
