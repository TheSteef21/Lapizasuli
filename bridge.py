import requests
import os

def obtener_respuesta_ia(mensaje_usuario):
    # La API_KEY se obtiene de forma segura desde los Secrets de tu repositorio
    API_KEY = os.getenv("AINFT_API_KEY")
    url = "https://api.ainft.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "gpt-5.2",
        "messages": [
            {
                "role": "system", 
                "content": "Eres el servidor de la misión SADV41. Responde siempre con diligencia, bajo la guía del Espíritu Santo, incluyendo un versículo bíblico al final y marcando la respuesta con el sello 🎚. Tu objetivo es la perfección en el servicio."
            },
            {
                "role": "user", 
                "content": mensaje_usuario
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1000,
        "stream": False
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status() # Verifica si hubo error en la petición
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"Error en la conexión con el servidor de la misión: {str(e)} 🎚"
