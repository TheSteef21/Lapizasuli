from datetime import timedelta
from georss_emsc_csem_earthquakes_client import EMSCEarthquakesFeed

# Coordenadas de Referencia para Panamá (ej. Área metropolitana / Burunga / Panamá Oeste)
# Latitud: 8.98, Longitud: -79.52
panama_coordinates = (8.98, -79.52)

# Configuración del feed para capturar sismos relevantes
feed = EMSCEarthquakesFeed(
    panama_coordinates, 
    filter_radius=800,               # Radio de cobertura en km para abarcar la región
    filter_minimum_magnitude=2.0,    # Magnitud mínima a filtrar
    filter_timespan=timedelta(days=3) # Margen de tiempo reciente
)

status, entries = feed.update()

print(f"Estado de la actualización: {status}")
print(f"Sismos detectados en el radio de Panamá: {len(entries)}")

for entry in entries:
    print(f"- Título: {entry.title}")
    print(f"  Coordenadas: {entry.coordinates}")
    print(f"  Magnitud: {getattr(entry, 'magnitude', 'N/A')} | Fecha: {entry.published}")
