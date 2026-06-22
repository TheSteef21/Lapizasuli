import os
from fastapi import FastAPI
import requests

app = FastAPI()

# He cambiado AINFT_API_KEY por AI_API_KEY para que coincida con tu configuración en Render
API_KEY = os.getenv("AI_API_KEY") 

@app.post("/api/ask-ia")
async def ask_ia(data: dict):
    # Asegúrate de que el frontend envíe 'pregunta' en el JSON
    pregunta = data.get("pregunta")
    
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
    return response.json()
