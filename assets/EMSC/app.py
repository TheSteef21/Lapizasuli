from datetime import timedelta
from fastapi import FastAPI
from georss_emsc_csem_earthquakes_client import EMSCEarthquakesFeed

app = FastAPI()

@app.get("/api/sismos-panama")
def obtener_sismos_panama():
    # Coordenadas de Referencia para Panamá (Burunga / Panamá Oeste)
    panama_coordinates = (8.98, -79.52)
    
    feed = EMSCEarthquakesFeed(
        panama_coordinates, 
        filter_radius=800,
        filter_minimum_magnitude=2.0,
        filter_timespan=timedelta(days=3)
    )
    
    status, entries = feed.update()
    
    eventos = []
    if entries:
        for entry in entries:
            eventos.append({
                "titulo": entry.title,
                "coordenadas": getattr(entry, 'coordinates', None),
                "magnitud": getattr(entry, 'magnitude', 'N/A'),
                "fecha": str(getattr(entry, 'published', 'N/A'))
            })
            
    return {
        "status": status,
        "total": len(eventos),
        "eventos": eventos
    }
