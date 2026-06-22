import os
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir que tu frontend hable con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, podrías cambiar "*" por la URL de tu web
    allow_methods=["*"],
    allow_headers=["*"],
)

# Esto lee la variable configurada en Render
API_KEY = os.getenv("AI_API_KEY")

@app.post("/api/ask-ia")
async def ask_ia(data: dict):
    # Capturamos la pregunta enviada desde aib.js
    pregunta = data.get("pregunta")
    
    if not pregunta:
        return {"error": "No se recibió ninguna pregunta."}

    # Hacemos la petición a la API de AINFT
    response = requests.post(
        "https://api.ainft.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-5.2",
            "messages": [{"role": "user", "content": pregunta}],
            "temperature": 0.7,
            "max_tokens": 1000
        },
    )
    
    # Devolvemos la respuesta tal cual llega de la API
    return response.json()
