from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app) # Permite peticiones desde tu frontend HTML

B_AI_API_KEY = 'sk-2mh9fxv12416jihj82urhv7pntzza4l4'

@app.route('/api/ask-ia', methods=['POST'])
def ask_ia():
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
        print(f"Error: {e}")
        return jsonify({'error': 'Fallo en la arquitectura neural SADV41'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
