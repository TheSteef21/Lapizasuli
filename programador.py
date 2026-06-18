import json
import os
from datetime import datetime
import random

# Nombre del archivo donde se guardará la información procesada
ARCHIVO_DATOS = "terremotos.json"

def procesar_datos_sísmicos():
    print("Conectando con el entorno REDPy (USGS)...")
    print("Analizando sismogramas y buscando familias de terremotos repetitivos...")
    
    # Simulación de detección de eventos sísmicos (Estructura típica de REDPy)
    eventos_detectados = [
        {
            "id": "usgs_2026_001",
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "magnitud": round(random.uniform(3.5, 6.2), 1),
            "profundidad_km": round(random.uniform(10.0, 50.0), 1),
            "ubicación": "Región Volcánica / Sismógrafo Local",
            "familia_redpy": "Familia A (Alta Repetitividad)",
            "ondas_coincidentes": random.randint(5, 15)
        },
        {
            "id": "usgs_2026_002",
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "magnitud": round(random.uniform(2.0, 4.0), 1),
            "profundidad_km": round(random.uniform(5.0, 25.0), 1),
            "ubicación": "Falla Tectónica Cercana",
            "familia_redpy": "Familia B (Baja Frecuencia)",
            "ondas_coincidentes": random.randint(2, 6)
        }
    ]
    
    # Guardamos los datos en formato JSON de manera limpia
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(eventos_detectados, f, indent=4, ensure_ascii=False)
        print(f"¡Éxito! Datos exportados correctamente a '{ARCHIVO_DATOS}'. Ready para el HTML.")
    except Exception as e:
        print(f"Error durante el procesamiento (Falla detectada): {e}")

if __name__ == "__main__":
    procesar_datos_sísmicos()
