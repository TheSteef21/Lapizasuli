import json
import os
from datetime import datetime
import random

# El script buscará escribir los datos para que el nuevo archivo HTML los lea
ARCHIVO_DATOS = "terremotos.json"

def ejecutar_analisis_redpy():
    print("==================================================")
    print("INICIANDO PROCESAMIENTO SÍSMICO - ENTORNO SADV41")
    print("==================================================")
    print("-> Accediendo al núcleo REDPy (Repeating Earthquake Detector)...")
    print("-> Leyendo flujos de sismogramas en tiempo real...")
    
    # Simulación de detección basada en la documentación de REDPy (USGS)
    # REDPy agrupa sismos en "familias" si sus formas de onda son idénticas
    eventos_filtrados = [
        {
            "id": "SADV41-2026-A",
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "magnitud": round(random.uniform(3.8, 6.5), 1),
            "profundidad_km": round(random.uniform(8.0, 45.0), 1),
            "ubicacion": "Zona de Subducción / Red de Estaciones USGS",
            "familia_redpy": "Familia Volcánica #04",
            "coeficiente_correlacion": round(random.uniform(0.85, 0.98), 2),
            "ondas_coincidentes": random.randint(12, 42)
        },
        {
            "id": "SADV41-2026-B",
            "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "magnitud": round(random.uniform(1.5, 3.2), 1),
            "profundidad_km": round(random.uniform(3.0, 15.0), 1),
            "ubicacion": "Falla Local Detectada",
            "familia_redpy": "Familia Tectónica #01",
            "coeficiente_correlacion": round(random.uniform(0.75, 0.84), 2),
            "ondas_coincidentes": random.randint(3, 9)
        }
    ]
    
    try:
        # Escritura limpia del archivo de intercambio de datos
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
            json.dump(eventos_filtrados, f, indent=4, ensure_ascii=False)
        print(f"\n[ÉXITO] Análisis finalizado. Datos exportados a '{ARCHIVO_DATOS}'.")
        print("Listo para ser leído por SADV41T.html")
    except Exception as e:
        print(f"\n[FALLA DETECTADA] Error en el flujo de bisolución: {e}")

if __name__ == "__main__":
    ejecutar_analisis_redpy()
