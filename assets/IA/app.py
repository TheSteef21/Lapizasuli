from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) # Permite peticiones desde tu frontend HTML

# 🛡️ SEGURIDAD SADV41: Obtenemos la clave de las variables de entorno de Render
B_AI_API_KEY = os.environ.get('AI_API_KEY') 

@app.route('/api/ask-ia', methods=['POST'])
def ask_ia():
    # Verificación de seguridad por si la variable de entorno no está configurada
    if not B_AI_API_KEY:
        print("Error: La API Key no está configurada en las variables de entorno.")
        return jsonify({'error': 'Fallo de configuración en el servidor'}), 500

    data = request.get_json()
    pregunta = data.get('pregunta')

    if not pregunta:
        return jsonify({'error': 'La pregunta es requerida'}), 400

    headers = {
        'Authorization': f'Bearer {B_AI_API_KEY}',
        'Content-Type': 'application/json',
    }

    payload = {
        'model': 'gpt-5.2',
        'messages': [
            {'role': 'system', 'content': 'Eres el Asistente IA de la Logia SADV41, experto en CasaCrypto y GSADV41.'},
            {'role': 'user', 'content': pregunta}
        ],
        'stream': False,
        'temperature': 0.7,
        'max_tokens': 1000
    }

    try:
        response = requests.post('https://api.b.ai/v1/chat/completions', headers=headers, json=payload)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        print(f"Error en la conexión neuronal: {e}")
        return jsonify({'error': 'Fallo en la arquitectura neural SADV41'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    # NOTA: En Render (producción), no se suele usar app.run(), sino un servidor WSGI como Gunicorn.
    app.run(host='0.0.0.0', port=port)
