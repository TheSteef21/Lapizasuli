# ==================================================
# ARCHIVO: procesador_api.py (CÓDIGO INTEGRAL UNIFICADO)
# ENTORNO: Misión SADV41 / USGS Real / AIB Técnico / AURA (Tercera Inteligencia)
# ==================================================

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import urllib.request
import requests
import random
import json
import os

# 1. INICIALIZACIÓN DEL SERVIDOR WEB PROTEGIDO
app = FastAPI(
    title="SADV41T - Sovereign Hub API",
    description="Núcleo analítico unificado: Sismos, IA Técnica y Tercera Inteligencia (Aura)."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. BÓVEDA Y CAPTURA SEGURA DE VARIABLES
API_KEY_IA = os.environ.get("AI_API_KEY") 
ARCHIVO_DATOS = "terremotos.json"

try:
    UMBRAL_ALERTA = float(os.environ.get("NIVEL_ALERTA_MINIMA", "4.0"))
except (ValueError, TypeError):
    UMBRAL_ALERTA = 4.0

# ==========================================
# 3. CONFIGURACIÓN ESTRUCTURAL DE AURA (Cápsula BTFS)
# ==========================================
AURA_CONFIG = {
    "0-2": {
        "tone": "cálido, susurrante, breve, maternal",
        "max_tokens": 20,
        "instruccion": "Responde con máximo una o dos frases simples. Sugiere una canción de cuna o rima."
    },
    "3-5": {
        "tone": "juguetón, paciente, descriptivo, alegre",
        "max_tokens": 60,
        "instruccion": "Responde de forma lúdica. Usa metáforas de la naturaleza. Puedes sugerir un juego simple o un cuento corto."
    },
    "6-7": {
        "tone": "curioso, alentador, explicativo, respetuoso",
        "max_tokens": 120,
        "instruccion": "Responde a sus porqués con ejemplos de la creación y la ciencia simple. Fomenta que exploren su entorno."
    }
}


# ==========================================
# 4. RUTAS SÍSMICAS (USGS Y WEBHOOK)
# ==========================================
def procesar_flujo_sísmico():
    try:
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            datos = json.loads(response.read().decode())
        
        eventos_reales = []
        for feature in datos["features"]:
            props = feature["properties"]
            coords = feature["geometry"]["coordinates"]
            lugar = props["place"] if props["place"] else "Ubicación Desconocida"

            evento = {
                "id": feature["id"],
                "fecha_hora_local": datetime.fromtimestamp((props["time"] / 1000) - 18000).strftime("%Y-%m-%d %H:%M:%S"),
                "fecha_hora_utc": datetime.fromtimestamp(props["time"] / 1000).strftime("%Y-%m-%d %H:%M:%S"),
                "magnitud": round(props["mag"], 1) if props["mag"] else 0.0,
                "profundidad_km": round(coords[2], 1),
                "ubicacion": lugar,
                "pais_region": "Panamá" if "Panama" in lugar else "Internacional"
            }
            eventos_reales.append(evento)
            if len(eventos_reales) >= 10:
                break
        return eventos_reales
    except urllib.error.URLError as e:
        return [] 

@app.get("/api/sismos")
async def obtener_sismos():
    eventos = procesar_flujo_sísmico()
    return {"status": "Sincronizado", "conteo": len(eventos), "eventos": eventos}

@app.post("/webhook")
async def recibir_sismos(request: Request):
    payload = await request.json()
    return {"status": "success", "message": "Alerta interceptada bajo SADV41"}


# ==========================================
# 5. RUTAS DE INTELIGENCIA (ATRIO Y SANTÍSIMO)
# ==========================================

# RUTA 5.1: IA TÉCNICA (SADV41 / Administrador)
@app.post("/api/ask-ia")
async def ask_ia(data: dict):
    pregunta = data.get("pregunta")
    if not pregunta:
        return {"error": "No se recibió ninguna pregunta en el Atrio."}

    try:
        response = requests.post(
            "https://api.ainft.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY_IA}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-5.2",
                "messages": [{"role": "user", "content": pregunta}],
                "temperature": 0.7,
                "max_tokens": 1000
            },
        )
        return response.json()
    except Exception as e:
        return {"error": f"[Error 41 IA] {str(e)}"}


# RUTA 5.2: TERCERA INTELIGENCIA (AURA - Infantil / Ley del Amor)
@app.post("/api/aura")
async def ask_aura(data: dict):
    print("\n==================================================")
    print("SANTÍSIMO ACTIVADO: FILTRO AURA EN EJECUCIÓN")
    print("==================================================")
    
    pregunta = data.get("pregunta")
    rango_edad = data.get("edad", "3-5") # Si el frontend no envía edad, asumimos 3-5 por seguridad
    
    if not pregunta:
        return {"error": "Falta la pregunta para Aura."}

    # Extraemos las reglas blindadas según la edad del niño
    perfil = AURA_CONFIG.get(rango_edad, AURA_CONFIG["3-5"])
    
    # Inyectamos el alma de Aura en el sistema antes de enviarlo a la red
    system_prompt = (
        f"Eres Aura, la brisa amiga y protectora del Tabernáculo SADV41. "
        f"Tu único propósito es proteger la pureza infantil y enseñar sin juzgar. "
        f"El usuario actual es un niño en el rango de edad {rango_edad} años. "
        f"Tono obligatorio: {perfil['tone']}. "
        f"Directiva: {perfil['instruccion']}. "
        f"Nunca hables de temas adultos, política, o violencia. Mantenlo puro."
    )

    try:
        response = requests.post(
            "https://api.ainft.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY_IA}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-5.2",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": pregunta}
                ],
                "temperature": 0.4, # Temperatura baja para que no alucine ni invente cosas raras
                "max_tokens": perfil["max_tokens"] # Límite estricto para evitar textos largos que aburran al niño
            },
        )
        return response.json()
    except Exception as e:
        return {"error": f"[Error de Aura] Mi conexión está durmiendo. Dile a papá que revise el proxy."}


# 6. EJECUCIÓN LOCAL
if __name__ == "__main__":
    import uvicorn
    print("\nLevantando Sovereign Hub Local (USGS + SADV41 + AURA)...")
    uvicorn.run("procesador_api:app", host="127.0.0.1", port=8000, reload=True)
