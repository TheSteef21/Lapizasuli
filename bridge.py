import requests
import os

def obtener_respuesta_ia(mensaje_usuario):
    API_KEY = os.getenv("AINFT_API_KEY")
    url = "https://api.ainft.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-5.2",
        "messages": [{"role": "user", "content": f"SADV41 Directiva: {mensaje_usuario}"}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']
